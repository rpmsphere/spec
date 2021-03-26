Name:           fbreader-sugar
Summary:        Sugar activity wrapper for FBReader
Version:        0.12.2
Release:        1
License:        MIT
Source:         %{name}.zip
Group:          Sugar/Activities
BuildArch:	noarch
Requires:       sugar
Requires:       libsugarize
Requires:       fbreader

%description
A Sugar activity that launches FBReader within the Sugar environment.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/sugar/activities/FBReader.activity
chmod 755 bin/fbreader-activity
cp -a setup.py activity bin %{buildroot}%{_datadir}/sugar/activities/FBReader.activity

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/sugar/activities/FBReader.activity/setup.py

%clean
rm -rf %{buildroot}

%files
%{_datadir}/sugar/activities/FBReader.activity

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.12.2
- Rebuild for Fedora
