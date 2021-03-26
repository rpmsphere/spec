Name:           hellanzb
Version:        0.13
Release:        10.1
Summary:        Hands-free nzb downloader and post processor
Group:          Networking/News
License:        BSD
URL:            http://www.hellanzb.com/trac/
Source0:        http://www.hellanzb.com/distfiles/hellanzb-%{version}.tar.gz
Patch0:         hellanzb-configuration-location3.patch
Patch1:         hellanzb-unrar-is-optional.patch
Patch2:         hellanzb-remove-bogus-shebang.patch
Patch3:         hellanzb-0.13-dont-attempt-multiple-groups.diff
# (ahmad) add patch from debian to fix compatibility with Twisted 10.0.0
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=573221
Patch4:         007-Twisted_10.0.0_compat.patch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildArch:      noarch
Requires:       parchive2
Requires:       python2-twisted
Requires:       python2-twisted-web
Requires:       python2-yenc

%description
hellanzb is an easy to use application designed to retrieve nzb files
and fully process them. The goal being to make getting files from Usenet
as hands-free as possible. Once fully installed, all that's required
is moving an nzb file to the queue directory. The rest: downloading,
par-checking, un-raring, etc. is done automatically by hellanzb.

%prep
%setup -q
%patch0
sed --in-place 's|\*DOCDIR\*|%{_docdir}|' Hellanzb/Core.py
sed --in-place 's|\*PKGNAME\*|%{name}|'   Hellanzb/Core.py
%patch1
%patch2
%patch3
%patch4 -p1 -b .twisted 

%build
python2 -c 'import setuptools; execfile("setup.py")' build

%install
mkdir -p %{buildroot}%{_sysconfdir}
python2 -c 'import setuptools; execfile("setup.py")' install --skip-build --root %{buildroot}

mv %{buildroot}%{_bindir}/%{name}.py %{buildroot}%{_bindir}/%{name}
rm %{buildroot}/usr/etc/%{name}.conf.sample

mv etc/hellanzb.conf.sample %{buildroot}/%{_docdir}/%{name}/

mkdir -p %{buildroot}%{_docdir}/%{name}/
cat > %{buildroot}%{_docdir}/%{name}/README.urpmi << EOF
Thanks for installing the %{_vendor} package of hellanzb. To configure
the client for use, copy /usr/share/doc/hellanzb/hellanzb.conf.sample to
$HOME/.hellanzb.conf and edit it appropriately. To start hellanzb, just
execute 'hellanzb -D' from a terminal. To enqueue nzbs, drop them in the queue
directory as configured in your $HOME/.hellanzb.conf.

If you want Hellanzb to automatically unrar downloaded files, install the 
'unrar' package from the %{_vendor} Nonfree repository.
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_docdir}/%{name}
%{python2_sitelib}/*
%{_bindir}/%{name}

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.13
- Rebuild for Fedora
* Tue Oct 22 2013 umeabot <umeabot> 0.13-10.mga4
+ Revision: 542678
- Mageia 4 Mass Rebuild
* Mon Oct 14 2013 pterjan <pterjan> 0.13-9.mga4
+ Revision: 497789
- Rebuild to add different pythonegg provides for python 2 and 3
* Sat Jan 12 2013 umeabot <umeabot> 0.13-8.mga3
+ Revision: 353168
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Fri Apr 15 2011 ahmad <ahmad> 0.13-7.mga1
+ Revision: 85973
- drop README.urpmi and create it directly in the spec (this way %%_vendor macro
  can be used)
* Fri Apr 15 2011 ennael <ennael> 0.13-6.mga1
+ Revision: 85960
- remove Mandriva occurence
* Tue Apr 12 2011 ennael <ennael> 0.13-5.mga1
+ Revision: 84048
- clean spec file
- imported package hellanzb
* Fri Nov 12 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 0.13-5mdv2011.0
+ Revision: 596963
- rebuild for python 2.7
* Wed Jun 16 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.13-4mdv2010.1
+ Revision: 548176
- add patch from debian to fix compatibility with Twisted 10.0.0
* Mon Mar 29 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.13-3mdv2010.1
+ Revision: 528812
- fix README.urpmi file, it shouldn't mention Fedora
- clean spec
* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.13-2mdv2010.0
+ Revision: 437864
- rebuild
* Thu Mar 05 2009 Jérôme Soyer <saispo@mandriva.org> 0.13-1mdv2009.1
+ Revision: 349030
- Fix python files
- import hellanzb
