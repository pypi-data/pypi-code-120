"""Functions for post-processing EN 17037 daylight outputs."""
import json
import os

from .annual import filter_schedule_by_hours, _process_input_folder


def _daylight_autonomy(values, occ_pattern, threshold, total_hours):
    """Calculate annual daylight autonomy for a sensor.

    Args:
        values: Hourly illuminance values as numbers.
        occ_pattern: A list of 0 and 1 values for hours of occupancy.
        threshold: Threshold value for daylight autonomy.
        total_hours: An integer for the total number of occupied hours,
            which can be used to avoid having to sum occ pattern each time.

    Returns:
        daylight autonomy
    """
    da = 0
    for is_occ, value in zip(occ_pattern, values):
        if is_occ == 0:
            continue
        if value > threshold:
            da += 1

    return round(100.0 * da / total_hours, 2)


def en17037_metrics_to_files(
    ill_file, occ_pattern, output_folder, grid_name=None, total_hours=None
):
    """Compute annual EN 17037 metrics for an ill file and write the results to a folder.

    This function generates 6 different files for daylight autonomy based on the varying
    level of reccomendation in EN 17037.

    Args:
        ill_file: Path to an ill file generated by Radiance. The ill file should be
            tab separated and shot NOT have a header. The results for each sensor point
            should be available in a row and and each column should be the illuminance
            value for a sun_up_hour. The number of columns should match the number of
            sun up hours.
        occ_pattern: A list of 0 and 1 values for hours of occupancy.
        output_folder: An output folder where the results will be written to. The folder
            will be created if not exist.
        grid_name: An optional name for grid name which will be used to name the output
            files. If None the name of the input file will be used.
        total_hours: An integer for the total number of occupied hours in the
            occupancy schedule. If None, it will be assumed that all of the
            occupied hours are sun-up hours and are already accounted for
            in the the occ_pattern.
    """
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    recommendations = {
        'minimum_illuminance': {
            'minimum': 100,
            'medium': 300,
            'high': 500
        }
        ,
        'target_illuminance': {
            'minimum': 300,
            'medium': 500,
            'high': 750
        }
    }

    grid_name = grid_name or os.path.split(ill_file)[-1][-4:]
    da_folders = []

    for target_type, thresholds in recommendations.items():
        type_folder = os.path.join(output_folder, target_type)
        if not os.path.isdir(type_folder):
            os.makedirs(type_folder)

        for level, threshold in thresholds.items():
            level_folder = os.path.join(type_folder, level)
            if not os.path.isdir(level_folder):
                os.makedirs(level_folder)
        
            da_file = os.path.join(
                level_folder, 'da', '%s.da' % grid_name).replace('\\', '/')
            folder = os.path.dirname(da_file)
            if not os.path.isdir(folder):
                os.makedirs(folder)
            sda_file = os.path.join(
                level_folder, 'sda', '%s.sda' % grid_name).replace('\\', '/')
            folder = os.path.dirname(sda_file)
            if not os.path.isdir(folder):
                os.makedirs(folder)

            da = []
            with open(ill_file) as results, open(da_file, 'w') as daf:
                for pt_res in results:
                    values = (float(res) for res in pt_res.split())
                    dar = _daylight_autonomy(values, occ_pattern, threshold, total_hours)
                    daf.write(str(dar) + '\n')
                    da.append(dar)

            space_target = 50 if target_type == 'target_illuminance' else 95
            pass_fail = [int(val > space_target) for val in da]

            sda = sum(pass_fail) / len(pass_fail)
            with open(sda_file, 'w') as sdaf:
                sdaf.write(str(sda))

            da_folders.append(os.path.join(level_folder, 'da'))

    return da_folders


# TODO - support a list of schedules/schedule folder to match the input grids
def en17037_to_folder(
    results_folder, schedule, grids_filter='*', sub_folder='metrics'
        ):
    """Compute annual EN 17037 metrics in a folder and write them in a subfolder.

    This folder is an output folder of annual daylight recipe. Folder should include
    grids_info.json and sun-up-hours.txt - the script uses the list in grids_info.json
    to find the result files for each sensor grid.

    Args:
        results_folder: Results folder.
        schedule: An annual schedule for 8760 hours of the year as a list of values. This
            should be a daylight hours schedule.
        grids_filter: A pattern to filter the grids. By default all the grids will be
            processed.
        sub_folder: An optional relative path for subfolder to copy results files.
            Default: metrics

    Returns:
        str -- Path to results folder.

    """
    grids, sun_up_hours = _process_input_folder(results_folder, grids_filter)
    occ_pattern, total_occ = \
        filter_schedule_by_hours(sun_up_hours=sun_up_hours, schedule=schedule)

    if total_occ != 4380:
        raise ValueError('There are %s occupied hours in the schedule. According to '
            'EN 17037 the schedule must consist of the daylight hours which is defined '
            'as the half of the year with the largest quantity of daylight' % total_occ)

    metrics_folder = os.path.join(results_folder, sub_folder)
    if not os.path.isdir(metrics_folder):
        os.makedirs(metrics_folder)

    for grid in grids:
        ill_file = os.path.join(results_folder, '%s.ill' % grid['full_id'])
        da_folders = en17037_metrics_to_files(
            ill_file, occ_pattern, metrics_folder, grid['full_id'], total_occ
        )

    # copy info.json to all results folders
    for folder_name in da_folders:
        grid_info = os.path.join(metrics_folder, folder_name, 'grids_info.json')
        with open(grid_info, 'w') as outf:
            json.dump(grids, outf, indent=2)

    # create info for available results. This file will be used by honeybee-vtk for
    # results visualization
    config_file = os.path.join(metrics_folder, 'config.json')

    cfg = _annual_daylight_en17037_config()

    with open(config_file, 'w') as outf:
        json.dump(cfg, outf)

    return metrics_folder


def _annual_daylight_en17037_config():
    """Return vtk-config for annual daylight EN 17037. """
    cfg = {
        "data": [
            {
                "identifier": "Daylight Autonomy - target 300 lux",
                "object_type": "grid",
                "unit": "Percentage",
                "path": "target_illuminance/minimum/da",
                "hide": False,
                "legend_parameters": {
                    "hide_legend": False,
                    "min": 0,
                    "max": 100,
                    "color_set": "nuanced",
                },
            },
            {
                "identifier": "Daylight Autonomy - target 500 lux",
                "object_type": "grid",
                "unit": "Percentage",
                "path": "target_illuminance/medium/da",
                "hide": False,
                "legend_parameters": {
                    "hide_legend": False,
                    "min": 0,
                    "max": 100,
                    "color_set": "nuanced",
                },
            },
            {
                "identifier": "Daylight Autonomy - target 750 lux",
                "object_type": "grid",
                "unit": "Percentage",
                "path": "target_illuminance/high/da",
                "hide": False,
                "legend_parameters": {
                    "hide_legend": False,
                    "min": 0,
                    "max": 100,
                    "color_set": "nuanced",
                },
            },
            {
                "identifier": "Daylight Autonomy - minimum 100 lux",
                "object_type": "grid",
                "unit": "Percentage",
                "path": "minimum_illuminance/minimum/da",
                "hide": False,
                "legend_parameters": {
                    "hide_legend": False,
                    "min": 0,
                    "max": 100,
                    "color_set": "nuanced",
                },
            },
            {
                "identifier": "Daylight Autonomy - minimum 300 lux",
                "object_type": "grid",
                "unit": "Percentage",
                "path": "minimum_illuminance/medium/da",
                "hide": False,
                "legend_parameters": {
                    "hide_legend": False,
                    "min": 0,
                    "max": 100,
                    "color_set": "nuanced",
                },
            },
            {
                "identifier": "Daylight Autonomy - minimum 500 lux",
                "object_type": "grid",
                "unit": "Percentage",
                "path": "minimum_illuminance/high/da",
                "hide": False,
                "legend_parameters": {
                    "hide_legend": False,
                    "min": 0,
                    "max": 100,
                    "color_set": "nuanced",
                },
            },
        ]
    }

    return cfg
