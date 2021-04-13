%global debug_package %{nil}

Name:           ht
Version:        2.1.0
Release:        12.1
Summary:        Disassembler, object dumper and hex editor
License:        GPL-2.0
Group:          Development/Tools/Debuggers
URL:            http://hte.sourceforge.net/
Source:         http://sourceforge.net/projects/hte/files/ht-source/ht-%version.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  lzo-devel
BuildRequires:  ncurses-devel

%description
The HT editor is a file viewer, editor and analyzer for text, binary,
and (especially) executable files.

%prep
%setup -q -n ht-%version
sed -i '63i #include <cmath>' htapp.cc
sed -i '3027s|abs|fabs|' htapp.cc

%build
./configure --prefix=/usr --enable-release
sed -i 's|-pipe|-pipe -Wno-narrowing|' Makefile
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/ht %{buildroot}%{_bindir}/hte

%files
%_bindir/hte
%doc AUTHORS ChangeLog KNOWNBUGS NEWS README TODO

%changelog
* Fri Dec 16 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuild for Fedora
* Sat Jun 22 2013 jengelh@inai.de
- Provide the program under an altername name "hte" so as to
  continue to be able to install it alongside LyX in openSUSE 13.1
  (where lyx has a new requirement on tex4ht).
* Fri Jun 14 2013 jengelh@inai.de
- Update to new upstream release 2.0.22
  * Fixed selection of nodes in call chain
  * Added ability to view/edit 64 bit symbols and relocation for ELFs
  * Added new option "editor/scroll offset" which determines how many
  extra lines the cursor should be visible when scolling
  * Fixed loading of ELF files for alpha
* Thu Feb 28 2013 jengelh@inai.de
- Drop call to autoreconf; this is no longer necessary
* Fri Dec 21 2012 jengelh@inai.de
- Update to new upstream release 2.0.21
  * support new x86 opcodes (adcx, adox, clac, stac, rdseed)
  * fixed usage of unaliged pointers
  * ncurses API 6 support
- Add ht-no-date.diff
* Sun Mar  4 2012 jengelh@medozas.de
- Update to new upstream release 2.0.20
  * Last version had a bug preventing load of 32 bit ELFs
* Tue Feb 28 2012 jengelh@medozas.de
- Update to new upstream release 2.0.19
  * fixed a crash with the "follow" function on invalid addresses
  in analyser
  * AVX, AVX2, BMI, BMI2 and TBM instruction support on x86
  * fixed loading of ELF files with no section headers
* Mon Feb 13 2012 coolo@suse.com
- patch license to follow spdx.org standard
* Fri Dec  2 2011 coolo@suse.com
- add automake as buildrequire to avoid implicit dependency
* Mon Mar 28 2011 jengelh@medozas.de
- Enable detection of inverse hyperbolic math functions and make
  them available in the evaluator.
* Wed Mar 23 2011 jengelh@medozas.de
- Initial package for build.opensuse.org
