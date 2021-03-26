Name:           bloat
BuildRequires:  libx86emu-devel
License:        GPL v3 or later
Group:          System/Emulators/PC
Summary:        Boot loader test program
Version:        0.3
Release:        1
Source:         https://codeload.github.com/wfeldt/bloat/tar.gz/%{version}#/%{name}-%{version}.tar.gz
URL:            https://github.com/wfeldt/bloat

%description
A boot loader test program. Runs your current setup in an emulator and tells
you what happens.

%prep
%setup -q
rm git2log

%build
make BINDIR=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/bloat
%doc README COPYING

%changelog
* Fri Feb 14 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Mon Jan 31 2011 snwint@suse.de
- create VERSION and changelog from git repo
- bios: added 'get disk type' and dummy 'disk write' functions
- detect kernel start
- added timer function
- translate dos chars to utf8
- add keyboard input
- detect gfxboot code
- increase default instruction count
- partition table parser supports now really complex setups
* Wed Apr  8 2009 snwint@suse.de
- adjusted to latest libx86emu
- lots of new logging flags
