Name:    dwdiff       
Version: 2.1.4
Release: 1
Summary: Front end to diff for comparing on a per word basis
License: GPLv3
URL:     https://os.ghalkes.nl/dwdiff.html
Source0: https://os.ghalkes.nl/dist/%{name}-%{version}.tar.bz2
Requires: diffutils
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: libicu-devel
Patch0: dwdiff-localedir.patch

%description
dwdiff is a front-end for the diff program that operates at the word level
instead of the line level. It is different from wdiff in that it allows the
user to specify what should be considered whitespace, and in that it takes an
optional list of characters that should be considered delimiters. Delimiters
are single characters that are treated as if they are words, even when there
is no whitespace separating them from preceding words or delimiters. 

%prep
%setup -q
#patch0 -p1 -b .localedir

%build
#dwdiff uses its own custom configure script
./configure --prefix=%{_prefix} \
            --binddir=%{_datadir}/locale \
            --docdir='share/doc/dwdiff' \
            CFLAGS="%{optflags}"
make 

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %{name}
#get rid of manpages other than UTF8
rm -rf %{buildroot}%{_mandir}/nl.ISO8859-1/man1/
rm -rf %{buildroot}%{_mandir}/nl.ISO8859-15/man1/
mkdir %{buildroot}%{_mandir}/man1/nl/
mv %{buildroot}%{_mandir}/nl.UTF-8/man1/dwdiff.1 %{buildroot}%{_mandir}/nl/man1/dwdiff.1
mv %{buildroot}%{_mandir}/nl.UTF-8/man1/dwfilter.1 %{buildroot}%{_mandir}/nl/man1/dwfilter.1
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%files -f %{name}.lang
%{_bindir}/dwdiff
%{_bindir}/dwfilter
%doc README COPYING Changelog 
%{_mandir}/man1/dwdiff.1*
%{_mandir}/man1/dwfilter.1*

%lang(nl) %{_mandir}/nl/man1/dwdiff.1*
%lang(nl) %{_mandir}/nl/man1/dwfilter.1*

%changelog
* Thu Dec 17 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.4
- Rebuilt for Fedora
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 2.0.9-19
- Rebuild for ICU 63
* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.9-17
- Rebuild for ICU 62
* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.9-16
- Rebuild for ICU 61.1
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 2.0.9-14
- Rebuild for ICU 60.1
* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 2.0.9-10
- rebuild for ICU 57.1
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 2.0.9-8
- rebuild for ICU 56.1
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 2.0.9-6
- rebuild for ICU 54.1
* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 2.0.9-5
- rebuild for ICU 53.1
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Thu Feb 13 2014 Jakub Hrozek <jhrozek@redhat.com> - 2.0.9-2
- Rebuild for new icu
* Mon Jan 20 2014 Jakub Hrozek <jhrozek@redhat.com> - 2.0.9-1
- New upstream release 2.0.9
* Tue Oct 01 2013 Jakub Hrozek <jhrozek@redhat.com> - 2.0.5-1
- New upstream release 2.0.7
* Mon Aug 05 2013 Jakub Hrozek <jhrozek@redhat.com> - 2.0.5-1
- New upstream release 2.0.5
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Sat Jan 26 2013 Kevin Fenzi <kevin@scrye.com> - 1.9-6
- Rebuild for new icu
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Wed Apr 15 2012 Jakub Hrozek <jhrozek@redhat.com> 1.9-5
- rebuild for new icu
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Fri Sep 16 2011 Caolán McNamara <caolanm@redhat.com> 1.9-3
- Resolves: rhbz#737232 rebuild for icu 4.8.1
* Mon Mar 07 2011 Caolán McNamara <caolanm@redhat.com> 1.9-2
- rebuild for icu 4.6
* Tue Feb 15 2011 Jakub Hrozek <jhrozek@redhat.com> 1.9-1
- New upstream release
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Fri Apr 2 2010 Caolán McNamara <caolanm@redhat.com> 1.7-3
- rebuild for icu 4.4
* Sun Mar 7 2010 Jakub Hrozek <jhrozek@redhat.com> 1.7-2
- New upstream release, changed license to GPLv3
* Sun Nov 8 2009 Jakub Hrozek <jhrozek@redhat.com> 1.6.1-1
- New upstream release
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Tue Dec 16 2008 Jakub Hrozek <jhrozek@redhat.com> 1.5-2
- Modify the localedir patch to allow build with fuzz=0 and version 1.5
* Tue Dec 16 2008 Jakub Hrozek <jhrozek@redhat.com> 1.5-1
- New upstream release
* Tue Dec 02 2008 Jakub Hrozek <jhrozek@redhat.com> 1.4-3
- Shorten summary so it's PackageKit friendly
* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.4-2
- Fix Patch0:/%%patch mismatch.
* Tue Jul 08 2008 Jakub Hrozek <jhrozek@redhat.com> 1.4-1
- New upstream release, which BR: libicu-devel
* Sun Feb 10 2008 Jakub Hrozek <jhrozek@redhat.com> 1.3-2
- Bump & rebuild for GCC 4.3
* Fri Dec 28 2007 Jakub Hrozek <jhrozek@redhat.com> 1.3-1
- New upstream 
* Tue Aug  21 2007 Jakub Hrozek <jhrozek@redhat.com> 1.2-5
Fix configure/build to make the package rebuild in mock
* Mon Aug  13 2007 Jakub Hrozek <jhrozek@redhat.com> 1.2-4
Clarified the license tag
* Thu Oct  12 2006 Jakub Hrozek <jhrozek@redhat.com> 1.2-3
Fixed NL manpages packaging according to BZ #209608 comment #3
* Sat Oct  7 2006 Jakub Hrozek <jhrozek@redhat.com> 1.2-2
Fixed bugs in the specfile according to BZ #209608 comment #1
* Fri Oct  6 2006 Jakub Hrozek <jhrozek@redhat.com> 1.2-1
-initial packaging
