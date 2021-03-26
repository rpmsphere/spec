%global _name DSBBg

Name:           dsbbg
Version:        0.1
Release:        1
Summary:        A simple Qt application to manage wallpapers
License:        BSD-like
Group:          User Interface/X
URL:            https://github.com/mrclksr/DSBBg
Source0:        %{_name}-%{version}.tar.gz
BuildRequires:  qt5-devel

%description
DSBBg is a simple Qt application to manage wallpapers, and to change
your desktop background using feh.

%prep
%setup -q -n %{_name}-%{version}  

%build
%qmake_qt5 PREFIX=/usr
sed -i '/$(STRIP)/d' Makefile
make

%install
mkdir -p %{buildroot}%{_bindir}
make install INSTALL_ROOT=%{buildroot}

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/applications/dsbbg.desktop
%{_datadir}/%{name}/dsbbg_de.qm

%changelog
* Tue Jan 07 2020 Wei-Lun Chao <blubat@member.fsf.org> - 0.1
- Rebuild for Fedora
