%undefine _debugsource_packages
%global __os_install_post %{nil}

Name: ngslang
Summary: Next Generation Shell
Version: 0.2.13
Release: 1
Group: Development/Language
License: GPL3
URL: https://github.com/ngs-lang/ngs
Source0: ngs-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: libffi-devel
BuildRequires: gc-devel
BuildRequires: peg-c
BuildRequires: pandoc

%description
Next Generation Shell is a powerful programming language and a shell designed
specifically for Ops. Because you deserve better.

%prep
%setup -q -n ngs-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}/usr/man %{buildroot}%{_mandir}

%files
%doc *.md LICENSE
%{_bindir}/*
%exclude /usr/doc/ngs/LICENSE
/usr/lib/ngs
%{_mandir}/man1/*

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.13
- Rebuild for Fedora
