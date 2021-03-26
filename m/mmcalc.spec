Name: mmcalc
Summary: Molar Mass Calculator
Version: 20170901
Release: 9.1
Group: Sciences/Chemistry
License: LGPL
URL: http://www.ogion76.name/home/mmcalc
Source: http://www.ogion76.name/home/mmcalc/%name-%version.tar.gz
BuildArch: noarch
BuildRequires: perl-Module-Build
BuildRequires: perl-File-BaseDir
BuildRequires: perl-Gtk2-Ex-Simple-List
BuildRequires: perl-Locale-Msgfmt
BuildRequires: perl-Locale-gettext
BuildRequires: perl-Archive-Extract-lzma-unlzma
BuildRequires: perl-Archive-Extract-tgz-tar-gzip
BuildRequires: perl-Archive-Extract-Z-uncompress
BuildRequires: perl-Archive-Extract-bz2-bunzip2
BuildRequires: perl-Archive-Extract-gz-gzip
BuildRequires: perl-Archive-Extract-tar-tar
BuildRequires: perl-Archive-Extract-tbz-tar-bunzip2
BuildRequires: perl-Archive-Extract-txz-tar-unxz
BuildRequires: perl-Archive-Extract-xz-unxz
BuildRequires: perl-Archive-Extract-zip-unzip
BuildRequires: perl-Archive-Extract
BuildRequires: perl-Gtk3-SimpleList

%description
This program calculates molar mass and percent of each
element for the given chemical formula.

The program contains perl module MMCalc.pm and two perl
scripts, mmcalc and gmmcalc.

mmcalc is a console version of calculator, while gmmcalc
is GUI version using Gtk2/Gtk3.

Examples of valid formulae: H2O, CuSO4*5h2o, hgcl2, c o,
In(NO3)3*4.5H2O, Rb16Cd25, 39Sb36.

Acronyms are also supported: [Zn2(dabco)(bdc)2]*4DMF,
Pd(acac)2, h4edta. It is possible to add, remove and
change the acronyms.

Using of parentheses, square brackets as well as braces
is acceptable.

%prep
%setup -q

%build
perl Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
rm -rf %{buildroot}
./Build pure_install
%find_lang %name

%files -f %name.lang
%doc README ChangeLog
%_bindir/*
%_datadir/%name
%_datadir/icons/hicolor/scalable/apps/%name.svg
%perl_privlib/vendor_perl/*.pm
%exclude %_libdir/perl5/vendor_perl/auto/MMCalc/.packlist
%_datadir/applications/g%{name}*.desktop

%changelog
* Wed Mar 28 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20170901
- Rebuild for Fedora
* Tue May 14 2013 Denis G. Samsonenko <ogion@altlinux.org> 20130514-alt1
- new version
* Sun Dec 02 2012 Denis G. Samsonenko <ogion@altlinux.org> 20121202-alt1
- new version
* Thu Aug 30 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120830-alt1
- new version
- mmcalc.desktop and mmcalc.svg are now packed into source tar.gz
* Tue Aug 21 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120821-alt1
- new version
- changelog fixed
* Wed Aug 15 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120815-alt1
- new version
* Tue Aug 14 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120814-alt1
- new version
* Mon Aug 13 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120813-alt1
- new version
* Sun Aug 12 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120811-alt2
- ChangeLog fixed
* Sun Aug 12 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120811-alt1
- new version
* Wed Aug 08 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120808-alt1
- new version
* Fri Aug 03 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120802-alt1
- new version
* Tue Sep 13 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110913-alt1
- new version
- add icon
- fix Desktop Entry
* Wed Sep 07 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110804-alt1
- build for Sisyphus
- adapt to use git and gear
* Fri Apr 08 2011 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20110804-alt0.sdg1
- new version
* Fri Apr 08 2011 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20110408-alt0.sdg1
- new version
* Fri Apr 01 2011 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20110330-alt0.sdg2
- little fix in files section in spec file
* Wed Mar 30 2011 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20110330-alt0.sdg1
- new version
* Sat Nov 20 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20101120-alt0.sdg1
- new version
* Sun Sep 05 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100905-alt0.sdg1
- new version
* Mon Jul 26 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100726-alt0.sdg1
- new version
- spec clean up
* Sat Jul 24 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100724-alt0.sdg1
- Build.PL (Module::Build) is used insted of Makefile.PL
- license is changed to LGPL
* Tue Jul 13 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100713-alt0.sdg1
- new version
* Sun Jul 11 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100711-alt0.sdg1
- new version
* Fri Jul 09 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100709-alt0.sdg1
- new version
* Thu Jul 08 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100708-alt0.sdg1
- new version
- minor changes in description
* Tue Jul 06 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100706-alt0.sdg1
- principle functionality realized
- README and ChangeLog added
* Fri May 07 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100507-alt0.sdg1
- new version
* Wed Mar 24 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100324-alt0.sdg1
- use Makefile.PL
* Tue Feb 16 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100216-alt0.sdg1
- initial build for ALTLinux
