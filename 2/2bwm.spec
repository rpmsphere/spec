%undefine _debugsource_packages

Name:           2bwm
Version:        0.3
Release:        1
Summary:        A fast floating WM
Group:          User Interface/Desktops
License:        ISC
URL:            https://github.com/venam/2bwm
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-xrm-devel

%description
2bWM with the particularity of having 2 borders, written over the XCB library
and derived from mcwm written by Michael Cardell. In 2bWM everything is
accessible from the keyboard but a pointing device can be used for move,
resize and raise/lower.

%prep
%setup -q

%build
%make_build

%install
%make_install PREFIX=/usr

%files
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
