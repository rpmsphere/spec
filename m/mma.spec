Name:		mma
Version:	21.09.2
Release:	1
Summary:	MIDI Accompaniment Generator
License:	GPL
URL:		https://www.mellowood.ca/mma/
Source0:	mma-devl.%{version}.tar.gz
Source1:	mma-bin-21.09.setup.py
Source2:	mma-bin-20.12.mma.py
Patch1:		mma-bin-21.09-pythonpath.patch
BuildArch: noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

%description
MMA is a accompaniment generator -- it creates midi tracks for a soloist to
perform with. User supplied files contain pattern selections, chords,
and MMA directives.

%prep
%setup -q -n %{name}-bin-%{version}
#%patch0 -p0
%patch1 -p0
find * -name '#*#' -exec rm {} \;
find * -type f -name '*.pyc' -exec rm {} \;
find * -type d -name '__pycache__' -depth -exec rmdir {} \;
mv includes lib plugins MMA
cp %{SOURCE1} setup.py
mkdir cli
cp %{SOURCE2} cli/mma

%build
python3 ./setup.py build

%install
rm -rf %{buildroot}
python3 ./setup.py install --root=%{buildroot} --skip-build --no-compile
# We're not fully pip compliant.
rm -fr %{buildroot}/%{python3_sitelib}/%{name}-*.egg-info

# Need to do this again, since setup install mangles the hashbang.
install %{SOURCE2} %{buildroot}/%{_bindir}/mma

%{__cp} -p text/README README
%{__cp} -p text/COPYING COPYING
%{__cp} -p text/CHANGES-21 CHANGES
%{__mv} docs/html html
mkdir -p %{buildroot}%{_mandir}/man1
%{__cp} -p docs/man/* %{buildroot}%{_mandir}/man1

%post
%{_bindir}/mma -G

%files
%doc README COPYING CHANGES text html
%{_bindir}/*
%{_mandir}/man1/*
%{python3_sitelib}/MMA
%{_datadir}/%{name}

%changelog
* Sun Dec 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 21.09.2
- Rebuilt for Fedora
* Thu Sep 30 2021 Johan Vromans <jvromans@squirrel.nl> - 21.09-1
- Upgrade to upstream 21.09.
* Sun Jul 18 2021 Johan Vromans <jvromans@squirrel.nl> - 20.12.4-1
- Upgrade to upstream 20.12.4.
* Mon May 24 2021 Johan Vromans <jvromans@squirrel.nl> - 20.12.3-1
- Upgrade to upstream 20.12.3.
* Mon Apr 05 2021 Johan Vromans <jvromans@squirrel.nl> - 20.12.2-1
- Upgrade to upstream 20.12.2.
* Sun Jan 24 2021 Johan Vromans <jvromans@squirrel.nl> - 20.12.1-1
- Upgrade to upstream 20.12.1.
* Wed Dec 09 2020 Johan Vromans <jvromans@squirrel.nl> - 20.12-1
- Upgrade to upstream 20.12.
* Fri Dec 04 2020 Johan Vromans <jvromans@squirrel.nl> - 20.02f-4
- Install in the standard file hierarchy.
* Tue Nov 17 2020 Johan Vromans <jvromans@squirrel.nl> - 20.02f-3
- Upgrade to new upstream version.
* Mon Sep 14 2020 Johan Vromans <jvromans@squirrel.nl> - 20.02e-3
- Upgrade to new upstream version.
* Thu Sep 10 2020 Johan Vromans <jvromans@squirrel.nl> - 20.02d-3
- Fix python3 'file' call in mma-gb.
* Tue Jun 02 2020 Johan Vromans <jvromans@squirrel.nl> - 20.02d-2
- Upgrade to new upstream version.
* Wed May 06 2020 Johan Vromans <jvromans@squirrel.nl> - 20.02c-2
- Upgrade to new upstream version.
* Thu Apr 23 2020 Johan Vromans <jvromans@squirrel.nl> - 20.02b-2
- Upgrade to new upstream version.
* Tue Apr 07 2020 Johan Vromans <jvromans@squirrel.nl> - 20.02a-2
- Upgrade to new upstream version.
* Sat Feb 22 2020 Johan Vromans <jvromans@squirrel.nl> - 20.02-1
- Upgrade to new upstream version.
* Tue Jan 21 2020 Johan Vromans <jvromans@squirrel.nl> - 19.08.c-1
- Upgrade to new upstream version.
* Sun Oct 27 2019 Johan Vromans <jvromans@squirrel.nl> - 19.08.b-1
- Upgrade to new upstream version.
* Sun Oct  6 2019 Johan Vromans <jvromans@squirrel.nl> - 19.08a-1
- Upgrade to new upstream version.
* Sun Aug 04 2019 Johan Vromans <jvromans@squirrel.nl> - 19.08-1
- Upgrade to new upstream version.
* Wed Jul 10 2019 Johan Vromans <jvromans@squirrel.nl> - 19.07-1
- Upgrade to new upstream version.
* Thu Jun 16 2016 Johan Vromans <jvromans@squirrel.nl> - 16.02-1
- Upgrade to new upstream version.
* Mon Jan 04 2016 Johan Vromans <jvromans@squirrel.nl> - 15.012-1
- Upgrade to new upstream version.
* Fri Nov 27 2015 Johan Vromans <jvromans@squirrel.nl> - 15.09b-1
- Upgrade to new upstream version.
* Tue Oct 27 2015 Johan Vromans <jvromans@squirrel.nl> - 15.09a-1
- Upgrade to new upstream version.
* Mon Apr 27 2015 Johan Vromans <jvromans@squirrel.nl> - 15.01a-1
- Upgrade to new upstream version.
* Sun Aug 25 2013 Johan Vromans <jvromans@squirrel.nl> - 10.12c-1
- Upgrade to new upstream version.
* Sun Aug 18 2013 Johan Vromans <jvromans@squirrel.nl> - 10.12a-1
- Initial version for Fedora 17.
