Name:		sugar-jumble
Version:	22
Release:	1
Summary:	Jumble for Sugar
Group:		Sugar/Activities
License:	LGPLv3
Source:		jumble-22.xo
BuildRequires:	python2, sugar-toolkit
Requires:	sugar
BuildArch:	noarch
URL:		http://activities.sugarlabs.org/addon/4413

%description
In a jumble of 83 objects, the player has to locate 20.
Each deal is different. 

%prep
%setup -q -n Jumble.activity

%build
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --prefix=%{buildroot}%{_prefix}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/sugar/activities/Jumble.activity/setup.py
sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{_datadir}/sugar/activities/Jumble.activity/Jumble.py

%clean
rm -rf %{buildroot}

%files
%{sugaractivitydir}/Jumble.activity

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 22
- Rebuilt for Fedora
