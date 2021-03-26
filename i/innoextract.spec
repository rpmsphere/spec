Name:           innoextract
Version:        1.5
Release:        2.1
License:        zlib
Summary:        Tool to extract installers created by Inno Setup
URL:            http://constexpr.org/innoextract/
Group:          Applications/Archiving
Source:         http://constexpr.org/innoextract/files/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  xz-devel

%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. innoextract allows to extract such installers under
non-windows systems without running the actual installer using wine.

%prep
%setup -q

%build
%cmake \
	-DCMAKE_INSTALL_DATAROOTDIR="%{_datadir}" \
	-DCMAKE_INSTALL_MANDIR="%{_mandir}" \
	-DCMAKE_INSTALL_BINDIR="%{_bindir}"
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc README.md CHANGELOG VERSION
%{_bindir}/innoextract
%{_mandir}/man1/innoextract.1*

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuild for Fedora
* Thu Sep 24 2015 Daniel Scharrer <daniel@constexpr.org> - 1.5-1
- Bump version to 1.5 (new upstream release):
- Added support for Inno Setup 5.5.6 installers
- Added --include and --exclude-temp options to filter extracted files
- Improved handling of file collisions and added a --collisions option to control the behavior
- Added support for newer GOG.com multi-part installers via the --gog option
- Added support for building without iconv, using builtin conversions and/or Win32 API instead
- Various bug fixes and improvements
* Mon Mar 11 2013 Daniel Scharrer <daniel@constexpr.org> - 1.4-1
- Bump version to 1.4 (new upstream release):
- Fixed issues with the progress bar in sandbox environments
- Fixed extracting very large installers with 32-bit innoextract builds
- Improved handling
- The --list command-line option can now combined with --test or --extract
- The --version command-line option can now be modified with --quiet
  or --silent
- Added support for preserving timestamps of extracted files
  (enabled by default)
- Added a --timestamps (-T) command-line options to control or disable
  file timestamps
- Added an --output-dir (-d) command-line option to control where files
  are extracted
- Various bug fixes and tweaks
* Tue Jul 03 2012 Daniel Scharrer <daniel@constexpr.org> - 1.3-1
- bump version to 1.3:
- Respect --quiet and --silent for multi-file installers
- Compile in C++11 mode if supported
- Warn about unsupported setup data versions
- Add support for Inno Setup 5.5.0 installers
* Sun Mar 25 2012 Daniel Scharrer <daniel@constexpr.org> - 1.2-1
- created package
