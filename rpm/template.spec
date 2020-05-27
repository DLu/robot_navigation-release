%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-nav-2d-utils
Version:        0.2.6
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS nav_2d_utils package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-nav-2d-msgs
Requires:       ros-noetic-nav-core2
Requires:       ros-noetic-nav-grid
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf2-geometry-msgs
Requires:       ros-noetic-tf2-ros
Requires:       ros-noetic-xmlrpcpp
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-nav-2d-msgs
BuildRequires:  ros-noetic-nav-core2
BuildRequires:  ros-noetic-nav-grid
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-rosunit
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf2-geometry-msgs
BuildRequires:  ros-noetic-tf2-ros
BuildRequires:  ros-noetic-xmlrpcpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
A handful of useful utility functions for nav_core2 packages.

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
* Wed May 27 2020 David V. Lu!! <davidvlu@gmail.com> - 0.2.6-1
- Autogenerated by Bloom

