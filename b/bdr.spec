Name:           bdr
BuildRequires:  nasm
License:        GPL v3 or later
Group:          System/Boot
Summary:        Boot Drive Emulation
Version:        0.4
Release:        7.1
Source:         bdr-0.4.tar.bz2
URL:            https://github.com/wfeldt/bdr

%description
Emulates a boot drive. That is, makes a regular file available as BIOS drive during
system startup.

%prep
%setup -q
%ifarch aarch64
sed -i 's/elf32-i386/elf64-littleaarch64/' Makefile
%endif

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/bdr
%doc README

%changelog
* Mon Feb 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
* Wed Apr  8 2009 snwint@suse.de
- created package
