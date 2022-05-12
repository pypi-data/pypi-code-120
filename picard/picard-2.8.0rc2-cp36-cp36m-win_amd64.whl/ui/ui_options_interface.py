# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InterfaceOptionsPage(object):
    def setupUi(self, InterfaceOptionsPage):
        InterfaceOptionsPage.setObjectName("InterfaceOptionsPage")
        InterfaceOptionsPage.resize(466, 735)
        self.vboxlayout = QtWidgets.QVBoxLayout(InterfaceOptionsPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox = QtWidgets.QGroupBox(InterfaceOptionsPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolbar_show_labels = QtWidgets.QCheckBox(self.groupBox)
        self.toolbar_show_labels.setObjectName("toolbar_show_labels")
        self.verticalLayout_3.addWidget(self.toolbar_show_labels)
        self.show_menu_icons = QtWidgets.QCheckBox(self.groupBox)
        self.show_menu_icons.setObjectName("show_menu_icons")
        self.verticalLayout_3.addWidget(self.show_menu_icons)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ui_language = QtWidgets.QComboBox(self.groupBox)
        self.ui_language.setObjectName("ui_language")
        self.horizontalLayout.addWidget(self.ui_language)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_theme = QtWidgets.QLabel(self.groupBox)
        self.label_theme.setObjectName("label_theme")
        self.verticalLayout_3.addWidget(self.label_theme)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ui_theme = QtWidgets.QComboBox(self.groupBox)
        self.ui_theme.setObjectName("ui_theme")
        self.horizontalLayout_2.addWidget(self.ui_theme)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.vboxlayout.addWidget(self.groupBox)
        self.miscellaneous_box = QtWidgets.QGroupBox(InterfaceOptionsPage)
        self.miscellaneous_box.setObjectName("miscellaneous_box")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.miscellaneous_box)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.toolbar_multiselect = QtWidgets.QCheckBox(self.miscellaneous_box)
        self.toolbar_multiselect.setObjectName("toolbar_multiselect")
        self.vboxlayout1.addWidget(self.toolbar_multiselect)
        self.builtin_search = QtWidgets.QCheckBox(self.miscellaneous_box)
        self.builtin_search.setObjectName("builtin_search")
        self.vboxlayout1.addWidget(self.builtin_search)
        self.use_adv_search_syntax = QtWidgets.QCheckBox(self.miscellaneous_box)
        self.use_adv_search_syntax.setObjectName("use_adv_search_syntax")
        self.vboxlayout1.addWidget(self.use_adv_search_syntax)
        self.quit_confirmation = QtWidgets.QCheckBox(self.miscellaneous_box)
        self.quit_confirmation.setObjectName("quit_confirmation")
        self.vboxlayout1.addWidget(self.quit_confirmation)
        self.filebrowser_horizontal_autoscroll = QtWidgets.QCheckBox(self.miscellaneous_box)
        self.filebrowser_horizontal_autoscroll.setObjectName("filebrowser_horizontal_autoscroll")
        self.vboxlayout1.addWidget(self.filebrowser_horizontal_autoscroll)
        self.starting_directory = QtWidgets.QCheckBox(self.miscellaneous_box)
        self.starting_directory.setObjectName("starting_directory")
        self.vboxlayout1.addWidget(self.starting_directory)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.starting_directory_path = QtWidgets.QLineEdit(self.miscellaneous_box)
        self.starting_directory_path.setEnabled(False)
        self.starting_directory_path.setObjectName("starting_directory_path")
        self.horizontalLayout_4.addWidget(self.starting_directory_path)
        self.starting_directory_browse = QtWidgets.QPushButton(self.miscellaneous_box)
        self.starting_directory_browse.setEnabled(False)
        self.starting_directory_browse.setObjectName("starting_directory_browse")
        self.horizontalLayout_4.addWidget(self.starting_directory_browse)
        self.vboxlayout1.addLayout(self.horizontalLayout_4)
        self.ui_theme_container = QtWidgets.QWidget(self.miscellaneous_box)
        self.ui_theme_container.setEnabled(True)
        self.ui_theme_container.setObjectName("ui_theme_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ui_theme_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vboxlayout1.addWidget(self.ui_theme_container)
        self.vboxlayout.addWidget(self.miscellaneous_box)
        self.customize_toolbar_box = QtWidgets.QGroupBox(InterfaceOptionsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customize_toolbar_box.sizePolicy().hasHeightForWidth())
        self.customize_toolbar_box.setSizePolicy(sizePolicy)
        self.customize_toolbar_box.setObjectName("customize_toolbar_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.customize_toolbar_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolbar_layout_list = QtWidgets.QListWidget(self.customize_toolbar_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbar_layout_list.sizePolicy().hasHeightForWidth())
        self.toolbar_layout_list.setSizePolicy(sizePolicy)
        self.toolbar_layout_list.setObjectName("toolbar_layout_list")
        self.verticalLayout.addWidget(self.toolbar_layout_list)
        self.edit_button_box = QtWidgets.QWidget(self.customize_toolbar_box)
        self.edit_button_box.setObjectName("edit_button_box")
        self.edit_box_layout = QtWidgets.QHBoxLayout(self.edit_button_box)
        self.edit_box_layout.setContentsMargins(0, 0, 0, 0)
        self.edit_box_layout.setObjectName("edit_box_layout")
        self.add_button = QtWidgets.QToolButton(self.edit_button_box)
        self.add_button.setObjectName("add_button")
        self.edit_box_layout.addWidget(self.add_button)
        self.insert_separator_button = QtWidgets.QToolButton(self.edit_button_box)
        self.insert_separator_button.setObjectName("insert_separator_button")
        self.edit_box_layout.addWidget(self.insert_separator_button)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.edit_box_layout.addItem(spacerItem2)
        self.up_button = QtWidgets.QToolButton(self.edit_button_box)
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-up.png")
        self.up_button.setIcon(icon)
        self.up_button.setObjectName("up_button")
        self.edit_box_layout.addWidget(self.up_button)
        self.down_button = QtWidgets.QToolButton(self.edit_button_box)
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-down.png")
        self.down_button.setIcon(icon)
        self.down_button.setObjectName("down_button")
        self.edit_box_layout.addWidget(self.down_button)
        self.remove_button = QtWidgets.QToolButton(self.edit_button_box)
        self.remove_button.setObjectName("remove_button")
        self.edit_box_layout.addWidget(self.remove_button)
        self.verticalLayout.addWidget(self.edit_button_box)
        self.vboxlayout.addWidget(self.customize_toolbar_box)

        self.retranslateUi(InterfaceOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(InterfaceOptionsPage)
        InterfaceOptionsPage.setTabOrder(self.toolbar_show_labels, self.show_menu_icons)
        InterfaceOptionsPage.setTabOrder(self.show_menu_icons, self.ui_language)
        InterfaceOptionsPage.setTabOrder(self.ui_language, self.ui_theme)
        InterfaceOptionsPage.setTabOrder(self.ui_theme, self.toolbar_multiselect)
        InterfaceOptionsPage.setTabOrder(self.toolbar_multiselect, self.builtin_search)
        InterfaceOptionsPage.setTabOrder(self.builtin_search, self.use_adv_search_syntax)
        InterfaceOptionsPage.setTabOrder(self.use_adv_search_syntax, self.quit_confirmation)
        InterfaceOptionsPage.setTabOrder(self.quit_confirmation, self.filebrowser_horizontal_autoscroll)
        InterfaceOptionsPage.setTabOrder(self.filebrowser_horizontal_autoscroll, self.starting_directory)
        InterfaceOptionsPage.setTabOrder(self.starting_directory, self.starting_directory_path)
        InterfaceOptionsPage.setTabOrder(self.starting_directory_path, self.starting_directory_browse)
        InterfaceOptionsPage.setTabOrder(self.starting_directory_browse, self.toolbar_layout_list)
        InterfaceOptionsPage.setTabOrder(self.toolbar_layout_list, self.add_button)
        InterfaceOptionsPage.setTabOrder(self.add_button, self.insert_separator_button)
        InterfaceOptionsPage.setTabOrder(self.insert_separator_button, self.up_button)
        InterfaceOptionsPage.setTabOrder(self.up_button, self.down_button)
        InterfaceOptionsPage.setTabOrder(self.down_button, self.remove_button)

    def retranslateUi(self, InterfaceOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_("Appearance"))
        self.toolbar_show_labels.setText(_("Show text labels under icons"))
        self.show_menu_icons.setText(_("Show icons in menus"))
        self.label.setText(_("User interface language:"))
        self.label_theme.setText(_("User interface color theme:"))
        self.miscellaneous_box.setTitle(_("Miscellaneous"))
        self.toolbar_multiselect.setText(_("Allow selection of multiple directories"))
        self.builtin_search.setText(_("Use builtin search rather than looking in browser"))
        self.use_adv_search_syntax.setText(_("Use advanced query syntax"))
        self.quit_confirmation.setText(_("Show a quit confirmation dialog for unsaved changes"))
        self.filebrowser_horizontal_autoscroll.setText(_("Adjust horizontal position in file browser automatically"))
        self.starting_directory.setText(_("Begin browsing in the following directory:"))
        self.starting_directory_browse.setText(_("Browse..."))
        self.customize_toolbar_box.setTitle(_("Customize Action Toolbar"))
        self.add_button.setToolTip(_("Add a new button to Toolbar"))
        self.add_button.setText(_("Add Action"))
        self.insert_separator_button.setToolTip(_("Insert a separator"))
        self.insert_separator_button.setText(_("Add Separator"))
        self.up_button.setToolTip(_("Move selected item up"))
        self.down_button.setToolTip(_("Move selected item down"))
        self.remove_button.setToolTip(_("Remove button from toolbar"))
        self.remove_button.setText(_("Remove"))
