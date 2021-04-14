%undefine _debugsource_packages

Name:           2bwm
Version:        0.2git
Release:        1.1
Summary:        A fast floating WM
Group:          User Interface/Desktops
License:        ISC
URL:            https://github.com/venam/2bwm
Source0:        %{name}-master.zip
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
%setup -q -n %{name}-master

%build
%make_build

%install
%make_install PREFIX=/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Jun 21 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2git
- Rebuilt for Fedora
