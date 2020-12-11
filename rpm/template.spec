%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-nav-grid-pub-sub
Version:        0.3.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS nav_grid_pub_sub package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-map-msgs
Requires:       ros-noetic-nav-2d-msgs
Requires:       ros-noetic-nav-2d-utils
Requires:       ros-noetic-nav-core2
Requires:       ros-noetic-nav-grid
Requires:       ros-noetic-nav-grid-iterators
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-roscpp
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-map-msgs
BuildRequires:  ros-noetic-nav-2d-msgs
BuildRequires:  ros-noetic-nav-2d-utils
BuildRequires:  ros-noetic-nav-core2
BuildRequires:  ros-noetic-nav-grid
BuildRequires:  ros-noetic-nav-grid-iterators
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslint
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Publishers and Subscribers for nav_grid data.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Dec 11 2020 David V. Lu!! <davidvlu@gmail.com> - 0.3.0-1
- Autogenerated by Bloom

* Wed May 27 2020 David V. Lu!! <davidvlu@gmail.com> - 0.2.6-1
- Autogenerated by Bloom

