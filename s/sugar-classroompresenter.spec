%global sugaractivitydir /usr/share/sugar/activities

Name:           sugar-classroompresenter
Version:        beta1
Release:        1
Summary:        Classroom Presenter for Sugar
Group:          Sugar/Activities
License:        LGPLv3
Source0:        ClassroomPresenter-beta1.xo
Source1:        Classroom Presenter for the OLPC XO-1 Laptop.doc
BuildRequires:  python2, sugar-toolkit-gtk3
Requires:       sugar
BuildArch:      noarch

%description
Classroom Presenter for the OLPC XO-1 Laptop.

%prep
%setup -q -n ClassroomPresenter.activity
cp "%{SOURCE1}" .

%build
python2 setup.py build

%install
rm -rf %{buildroot}
#python2 setup.py build --prefix=%{buildroot}/usr
mkdir -p %{buildroot}%{_datadir}/sugar/activities/ClassroomPresenter.activity
cp -a * %{buildroot}%{_datadir}/sugar/activities/ClassroomPresenter.activity
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/sugar/activities/ClassroomPresenter.activity/setup.py

%files
%doc *.doc
%{sugaractivitydir}/ClassroomPresenter.activity

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - beta1
- Rebuilt for Fedora
