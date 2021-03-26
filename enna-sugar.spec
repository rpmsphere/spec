Name:           enna-sugar
Summary:        Sugar activity wrapper for Enna
Version:        0.1
Release:        2
License:        MIT
Source:         %{name}.zip
Group:          Sugar/Activities
BuildArch:	noarch
Requires:       sugar
Requires:       libsugarize
Requires:       enna

%description
A Sugar activity that launches Enna within the Sugar environment.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/sugar/activities/Enna.activity
chmod 755 bin/enna-activity
cp -a setup.py activity bin %{buildroot}%{_datadir}/sugar/activities/Enna.activity

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/Enna.activity

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Fri Feb 22 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1-2
- initial RPM for OSSII
