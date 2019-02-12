Name:           ros-indigo-dwb-critics
Version:        0.2.5
Release:        0%{?dist}
Summary:        ROS dwb_critics package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-angles
Requires:       ros-indigo-costmap-queue
Requires:       ros-indigo-dwb-local-planner
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-nav-2d-msgs
Requires:       ros-indigo-nav-2d-utils
Requires:       ros-indigo-nav-core2
Requires:       ros-indigo-nav-grid-iterators
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-costmap-queue
BuildRequires:  ros-indigo-dwb-local-planner
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-nav-2d-msgs
BuildRequires:  ros-indigo-nav-2d-utils
BuildRequires:  ros-indigo-nav-core2
BuildRequires:  ros-indigo-nav-grid-iterators
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslint
BuildRequires:  ros-indigo-sensor-msgs

%description
Implementations for dwb_local_planner TrajectoryCritic interface

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Feb 12 2019 David V. Lu!! <davidvlu@gmail.com> - 0.2.5-0
- Autogenerated by Bloom

* Wed Nov 21 2018 David V. Lu!! <davidvlu@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

* Wed Nov 21 2018 David V. Lu!! <davidvlu@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

* Wed Nov 21 2018 David V. Lu!! <davidvlu@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

