%global debug_package %{nil}
%define _name qTouchWeb

Name:          qtouchweb
Version:       20110307
Release:       1
Summary:       MeeTo Virtual Keyboard
Group:         System Environment/Libraries
License:       LGPLv2
URL:           https://github.com/penk/MeeTo/tree/master/qTouchWeb
Source0:       %{_name}.tar.gz
BuildRequires: qt4-devel

%description
A free virtual keyboard for use in tablet UX for MeeGo.

%prep
%setup -q -n %{_name}

%build
qmake-qt4
make

%install
rm -rf %{buildroot}
install -Dm755 src/%{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20110307
- Rebuild for Fedora
