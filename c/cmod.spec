Name: cmod
Version: 0.01
Release: 6.1
Summary: Modula compiler written in C
License: GPLv2
Group: Development/Languages
URL: https://github.com/redbrain/modc
Source0: modc-master.zip
BuildRequires: cmake
BuildRequires: flex-devel
BuildRequires: bison-devel

%description
Modula compiler written in C using flex and bison for linux i386 fork of
the java implmentation in Queens University Belfast.

%prep
%setup -q -n modc-master
sed -i 's|cmakedefine|define|' src/config.h.in.cmake

%build
%cmake
make

%install
install -Dm755 src/cmod %{buildroot}%{_bindir}/cmod

%files
%doc AUTHORS ChangeLog COPYING README testsuite/*
%{_bindir}/%{name}

%changelog
* Tue Oct 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.01
- Rebuilt for Fedora
