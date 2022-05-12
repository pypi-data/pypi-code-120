import datetime

from integrations.calculate_primary.common import logger
from integrations.calculate_primary.common import MOPrimaryEngagementUpdater
from integrations.SD_Lon.sdlon import sd_common


class SDPrimaryEngagementUpdater(MOPrimaryEngagementUpdater):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def remove_past(user_uuid, no_past, eng):
            if no_past and eng["validity"]["to"]:
                to = datetime.datetime.strptime(eng["validity"]["to"], "%Y-%m-%d")
                if to < datetime.datetime.now():
                    return False
            return True

        def remove_no_salary(eng):
            return not self._predicate_primary_is("no_salary", eng)

        def remove_no_salary_check(user_uuid, eng):
            return remove_no_salary(eng)

        def remove_no_salary_calculate(user_uuid, no_past, eng):
            return remove_no_salary(eng)

        def remove_missing_user_key(user_uuid, no_past, eng):
            return "user_key" in eng

        self.check_filters = [
            remove_no_salary_check,
        ]

        self.calculate_filters = [
            remove_past,
            remove_no_salary_calculate,
            remove_missing_user_key,
        ]

    def _find_primary_types(self):
        # Keys are; fixed_primary, primary, no_salary and non-primary
        primary_types = sd_common.primary_types(self.helper)
        primary = [
            primary_types["fixed_primary"],
            primary_types["primary"],
            primary_types["no_salary"],
        ]
        return primary_types, primary

    def _find_primary(self, mo_engagements):
        def non_integer_userkey(mo_engagement):
            try:
                # non-integer user keys should universally be status0, and as such
                # they should already have been filtered out, thus if they have not
                # been filtered out, they must have the wrong primary_type.
                int(mo_engagement["user_key"])
            except ValueError:
                self._fixup_status_0(mo_engagement)
                # Filter it out, as it should have been
                return False
            return True

        # Ensure that all mo_engagements have integer user_keys.
        mo_engagements = list(filter(non_integer_userkey, mo_engagements))

        if not mo_engagements:
            return None

        # The primary engagement is the engagement with the highest occupation rate.
        # - The occupation rate is found as 'fraction' on the engagement.
        #
        # If two engagements have the same occupation rate, the tie is broken by
        # picking the one with the lowest user-key integer.
        primary_engagement = max(
            mo_engagements,
            # Sort first by fraction, then reversely by user_key integer
            key=lambda eng: (eng.get("fraction") or 0, -int(eng["user_key"])),
        )
        return primary_engagement["uuid"]

    def _fixup_status_0(self, mo_engagement):
        logger.warning("Engagement type not status0. Will fix.")
        validity = mo_engagement["validity"]
        payload = {
            "type": "engagement",
            "uuid": mo_engagement["uuid"],
            "data": {
                "primary": {"uuid": self.primary_types["no_salary"]},
                "validity": validity,
            },
        }
        logger.debug("Status0 edit payload: {}".format(payload))
        if not self.dry_run:
            response = self.helper._mo_post("details/edit", payload)
            assert response.status_code == 200
            logger.info("Status0 fixed")
