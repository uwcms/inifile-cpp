# Build this using apx-rpmbuild.
%define name inicpp

Name:           %{name}-devel
Version:        %{version_rpm_spec_version}
Release:        %{version_rpm_spec_release}%{?dist}
Summary:        An INI file parser, as a C++ header file

License:        MIT
URL:            https://github.com/uwcms/inifile-cpp
Source0:        %{name}-%{version_rpm_spec_version}.tar.gz

BuildArch:      noarch
#BuildRequires:
#Requires:

%description
An ini file parser from https://github.com/Rookfighter/inifile-cpp

Versioning provided locally.

%global debug_package %{nil}

%prep
%setup -q


%build
# Nothing to do.

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}/%{_includedir}
install -D -m 0644 include/inicpp.h %{buildroot}/%{_includedir}/inicpp.h

%files
%{_includedir}/inicpp.h

%changelog
* Wed Jul  6 2022 Jesra Tikalsky <jtikalsky@hep.wisc.edu>
- Initial spec file
