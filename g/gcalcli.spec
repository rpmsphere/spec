Name:           gcalcli
Version:        4.0.0a4
Release:        3.1
License:        MIT License
BuildArch:      noarch
BuildRequires:  help2man python3-dateutil 
Requires:       python3-dateutil 
#Requires:       python3-gdata
Source:         http://gcalcli.googlecode.com/files/%{name}-%{version}.tar.gz
Group:          Productivity/Office/Organizers
Summary:        Google Calendar Command Line Interface

%description
gcalcli is a Python application that allows you to access your Google
Calendar from a command line. It's easy to get your agenda, search for
events, and quickly add new events. Additionally gcalcli can be used
as a reminder service to execute any application you want.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=/usr --root=%{buildroot}

sed -i 's|/usr/bin/python$|/usr/bin/python3|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{python3_sitelib}/%{name}*

%changelog
* Tue Apr 03 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.0a4
- Rebuild for Fedora
* Mon Feb 16 2009 mhrusecky@suse.cz
- Fixed fedora dependencies
* Mon Feb 16 2009 mhrusecky@suse.cz
- Initial package of gcalcli (version 1.4)
