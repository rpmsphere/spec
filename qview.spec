Name:           qview
Version:        3.0
Release:        1
Summary:        Practical and minimal image viewer
License:        GPL3
Group:          Graphics
URL:            https://interversehq.com/qview
Source0:        https://github.com/jurplel/qView/archive/%{version}.tar.gz#/qView-%{version}.tar.gz
BuildRequires:  qt5-devel

%description
qView is a Qt-based image viewer designed with minimalism and usability in mind.

%prep
%setup -q -n qView

%build
%qmake_qt5 PREFIX=/usr
make

%install
mkdir -p %{buildroot}%{_bindir}
make install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/applications/qView.desktop
%{_datadir}/licenses/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <blubat@member.fsf.org> - 3.0
- Rebuild for Fedora
