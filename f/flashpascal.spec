%undefine _debugsource_packages

Name: flashpascal
Summary: Pascal for Flash compiler
Version: 0.8
Release: 7.1
Group: Development/Languages
License: GPLv2
URL: https://flashpascal.sourceforge.net/
Source0: https://sourceforge.net/projects/flashpascal/files/flashpascal/FlashPascal-%{version}/FlashPascal-%{version}.zip
BuildRequires: fpc

%description
Flash Pascal is a Pascal like language compiler that build Flash (SWF) files.

%prep
%setup -q -n FlashPascal

%build
fpc src/FlashPascal.dpr

%install
install -Dm755 src/FlashPascal %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a dcu doc ppu samples units readme.txt %{buildroot}%{_datadir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Thu Jan 02 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuilt for Fedora
