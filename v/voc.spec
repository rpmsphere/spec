Name: voc
Summary: Vishap Oberon Compiler
Version: 2.1.0git
Release: 13.1
Group: Development/Language
License: GPLv3
URL: https://github.com/vishaps/voc
Source0: %{name}-master.zip
BuildRequires: glibc-static
BuildRequires: libX11-devel

%description
Ѵishap Oberon is a free and open source (GPLv3) implementation of the Oberon-2
language and libraries for use on conventional operating systems such as Linux,
BSD, Android, Mac and Windows.

Vishap's Oberon Compiler (voc) uses a C backend (gcc, clang or msc) to compile
Oberon programs under Unix, Mac or Windows. Vishap Oberon includes libraries
from the Ulm, oo2c and Ofront Oberon compilers, as well as default libraries
complying with the Oakwood Guidelines for Oberon-2 compilers.

%prep
%setup -q -n %{name}-master
sed -i '/addlibrary.sh/d' src/tools/make/oberon.mk
sed -i '/-s confidence/d' makefile

%build
make full

%install
make install INSTALLDIR=%{buildroot}/usr/libexec
mkdir -p %{buildroot}/etc/ld.so.conf.d %{buildroot}/etc/profile.d
echo %{_libexecdir}/%{name}/lib > %{buildroot}/etc/ld.so.conf.d/05vishap.conf
echo 'PATH=${PATH}:%{_libexecdir}/%{name}/bin' > %{buildroot}/etc/profile.d/%{name}.sh

%files
%doc LICENSE ReadMe.md triage/*.md triage/hints triage/quick_start
%{_libexecdir}/*
/etc/ld.so.conf.d/05vishap.conf
/etc/profile.d/%{name}.sh

%changelog
* Fri Oct 05 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0git
- Rebuilt for Fedora
* Thu Jan 29 2015 - N. Chilingarian <norayr [at] vishap.am>
- 1.1 release, see changelog.
* Thu Sep 18 2014 - N. Chilingarian <norayr [at] vishap.am>
- 1.0.1 release of voc, see CHANGES.md file for changes history
* Tue Sep 9 2014 - D. E. Evans <sinuhe@gnu.org>
- Initial 1.0 release.
