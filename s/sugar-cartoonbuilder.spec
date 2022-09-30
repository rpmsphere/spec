Name:		sugar-cartoonbuilder
Version:	11
Release:	2.1
Summary:	Cartoon Builder for Sugar
Group:		Sugar/Activities
License:	LGPLv3
Source:		cartoon_builder-11.xo
BuildRequires:	python3, sugar-toolkit-gtk3
Requires:	sugar
BuildArch:	noarch

%description
Make a cartoon by creating a sequence of poses inside a filmstrip.

%prep
%setup -q -n CartoonBuilder.activity
sed -i 's|sugar|sugar3|' setup.py

%build
python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --prefix=%{buildroot}%{_prefix}

sed -i 's|/usr/bin/python$|/usr/bin/python3|' %{buildroot}%{_datadir}/sugar/activities/CartoonBuilder.activity/setup.py
sed -i 's|%{buildroot}||' %{buildroot}%{_datadir}/applications/*.activity.desktop

%clean
rm -rf %{buildroot}

%files
%{sugaractivitydir}/CartoonBuilder.activity
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/applications/*.activity.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 11
- Rebuilt for Fedora
