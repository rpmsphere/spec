BuildRequires:  python2-devel
Name:           openark-kit
Version:        170
Release:        3.1
Source0:        %{name}-%{version}.tar.bz2
Patch:          %{name}-%{version}-socketpath.patch
License:        BSD
BuildArch:      noarch
Group:          Productivity/Databases/Tools
Summary:        Common utilities for MySQL
URL:            http://code.openark.org/forge/%{name}
Requires:       MySQL-python

%description
The openark kit provides common utilities to administer, diagnose and audit MySQL databases.

%prep
%setup -q
%patch -p0

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%define __record_arg --record
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT %__record_arg %{name}.files --install-data %{_datadir}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%doc INSTALL README

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 170
- Rebuild for Fedora
* Wed Dec 15 2010 lenz@grimmer.com
- Update to version 170 (new tools, new functionality), see
  http://code.openark.org/blog/mysql/openark-kit-rev-170-new-tools-new-functionality
- Updated socket path patch file
* Mon Apr 12 2010 lenz@grimmer.com
- Update to version 111
- Updated patch
* Mon Nov 30 2009 lenz@grimmer.com
- Initial version for the openSUSE Build Service (96)
- Applied patch to match the socket path name to the openSUSE
  default path
