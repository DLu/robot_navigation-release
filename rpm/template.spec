Name:           ros-melodic-nav-core-adapter
Version:        0.2.5
Release:        1%{?dist}
Summary:        ROS nav_core_adapter package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-costmap-2d
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-nav-2d-msgs
Requires:       ros-melodic-nav-2d-utils
Requires:       ros-melodic-nav-core
Requires:       ros-melodic-nav-core2
Requires:       ros-melodic-nav-grid
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-tf
Requires:       ros-melodic-visualization-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-costmap-2d
BuildRequires:  ros-melodic-dwb-critics
BuildRequires:  ros-melodic-dwb-local-planner
BuildRequires:  ros-melodic-dwb-plugins
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-nav-2d-msgs
BuildRequires:  ros-melodic-nav-2d-utils
BuildRequires:  ros-melodic-nav-core
BuildRequires:  ros-melodic-nav-core2
BuildRequires:  ros-melodic-nav-grid
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-roslint
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-visualization-msgs

%description
This package contains adapters for using `nav_core` plugins as `nav_core2`
plugins and vice versa (more or less). See README.md for more information.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Feb 19 2019 David V. Lu!! <davidvlu@gmail.com> - 0.2.5-1
- Autogenerated by Bloom

* Wed Feb 13 2019 David V. Lu!! <davidvlu@gmail.com> - 0.2.5-0
- Autogenerated by Bloom

* Tue Dec 04 2018 David V. Lu!! <davidvlu@gmail.com> - 0.2.4-0
- Autogenerated by Bloom

* Tue Dec 04 2018 David V. Lu!! <davidvlu@gmail.com> - 0.2.3-0
- Autogenerated by Bloom

