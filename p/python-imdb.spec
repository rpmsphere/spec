%define realname IMDbPY

Name:           python-imdb
Version:        5.1
Release:        9
Summary:        Retrieve and manage the data of the IMDb movie database
License:        GPLv2+   
URL:            http://imdbpy.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/imdbpy/%{realname}-%{version}.tar.gz
#use system beautifulsoup
Patch0:         %{name}-4.2-beautifulsoup.patch
Patch1:		%{name}-4.8.2-setup.patch
BuildRequires:  python2-devel, python2-setuptools, gettext, gcc

%global _description\
IMDbPY is a Python package useful to retrieve and manage the data of\
the IMDb movie database about movies, people, characters and companies.\
\
IMDbPY is mainly a tool intended for programmers and developers, but\
some example scripts are included.

%description %_description

%package -n python2-imdb
Summary: %summary
Requires:       python2-sqlobject, python2-lxml, python2-beautifulsoup
Requires:       python2-formencode, python2-sqlalchemy, python2-migrate
Provides:       IMDbPY = %{version}-%{release}
%{?python_provide:%python_provide python2-imdb}

%description -n python2-imdb %_description

%prep
%setup -qn %{realname}-%{version}
%patch0 -p0
%patch1 -p0

#patch removes need for bundled beautifulsoup, so let's remove it
rm -f imdb/parser/http/bsouplxml/_bsoup.py

#fix end-of-line-encoding
%{__sed} -i 's/\r//' docs/imdbpy.cfg

%build
%{__python2} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

#Don't include these as binaries, rather include them as examples in documentation
#See debian for reference 
rm -rf $RPM_BUILD_ROOT%{_bindir}

mv bin examples
chmod 0644 examples/*

#don't include these twice
rm -f $RPM_BUILD_ROOT%{_prefix}/doc/*
rm -f $RPM_BUILD_ROOT%{_prefix}/etc/*

for i in en it tr; do
        mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES/
        mv $RPM_BUILD_ROOT/%{python2_sitelib}/imdb/locale/$i/LC_MESSAGES/imdbpy.mo $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES/
done

#find_lang imdbpy

#files -n python2-imdb -f imdbpy.lang
%files -n python2-imdb
%doc docs/AUTHOR.txt docs/Changelog.txt docs/CONTRIBUTORS.txt docs/DISCLAIMER.txt docs/FAQS.txt docs/LICENSE.txt docs/README* docs/TODO.txt docs/imdbpy.cfg
%doc examples
%{python2_sitearch}/*
%{python2_sitelib}/*
%{_datadir}/locale/*/LC_MESSAGES/imdbpy.mo

%changelog
* Wed Jul 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 5.1
- Rebuilt for Fedora
* Wed Jul 25 2018 Gwyn Ciesla <limburgher@gmail.com> - 5.1-9
- Fix FTBFS.
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)
* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.1-5
- Python 2 binary package renamed to python2-imdb
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Fri Dec 09 2016 Jon Ciesla <limburgher@gmail.com> - 5.1-1
- Latest upstream.
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Wed Feb 24 2016 Jon Ciesla <limburgher@gmail.com> - 5.0-1
- Latest upstream.
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Fri Jan 25 2013 Jon Ciesla <limburgher@gmail.com> - 4.9-1
- New upstream.
- Requires fixes, BZ 904088.
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Tue Mar 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 4.8.2-2
- Fix IMDbPY Provides version-release.
* Mon Feb 20 2012 Jon Ciesla <limburgher@gmail.com> - 4.8.2-1
- New upstream.
- Using find_lang now. 
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Fri Jul 15 2011 Jon Ciesla <limb@jcomserv.net> - 4.7-1
- New upstream.
* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Wed Mar 24 2010 Jon Ciesla <limb@jcomserv.net> - 4.5.1-3
- Apply said patch.
* Wed Mar 24 2010 Jon Ciesla <limb@jcomserv.net> - 4.5.1-2
- Patch to fix setuptools behaviour.
* Tue Mar 23 2010 Jon Ciesla <limb@jcomserv.net> - 4.5.1-1
- New upstream, fixes data retrieval issue, BZ 576027, 576028.
* Wed Feb 03 2010 Jon Ciesla <limb@jcomserv.net> - 4.4-1
- New upstream, fixes data retrieval issue, BZ 539818.
* Wed Feb 03 2010 Jon Ciesla <limb@jcomserv.net> - 4.2-2
- Corrected 4.2 build.
* Fri Sep 26 2009 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 4.2-1
- New upstream release
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Apr 01 2009 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 4.0-5
- Fix typo in Provides:
* Wed Apr 01 2009 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 4.0-4
- Add Provides: upstream name
- Add missing python-setuptools buildrequires
* Wed Apr 01 2009 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 4.0-2
- New upstream release
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Sun Dec 22 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 3.8-3
- Add patch to use system BeautifulSoup
- Add beautifulsoup requires
- Fix bogus permission on cutils file
* Fri Dec 05 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 3.8-1
- Initial build
