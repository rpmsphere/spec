Name:		bin2iso
Summary:	Converts bin/cue images to ISO images
Version:	1.9b
Release:	4.1
URL:		http://users.andara.com/~doiron/bin2iso/
Source0:	bin2iso19b.zip
Patch0:		bin2iso-build.patch
License:	Freeware
Group:		Productivity/Multimedia/CD/Record
BuildRequires:	unzip dos2unix glibc-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-build

%description
bin2iso converts RAW format (.bin) files to ISO/WAV format.

Authors:
-------
    Bob Doiron <doiron@hfx.andara.com>

%prep
%setup -c -n bin2iso-%{version}
dos2unix bin2iso19b.c readme.txt
%patch0

%build
gcc %optflags -o bin2iso bin2iso19b.c

%install
rm -rf  $RPM_BUILD_ROOT
install -D -m0755 bin2iso $RPM_BUILD_ROOT%{_bindir}/bin2iso

%clean
rm -rf  $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%{_bindir}/bin2iso
%doc readme.txt

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9b
- Rebuilt for Fedora
* Thu Jan 19 2012 - joerg.lorenzen@ki.tng.de
- Initial package, version 1.9b
