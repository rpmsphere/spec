Summary:	A pure console visual file manager
Name:		xyzcmd
Version:	0.0.5
Release:	8.1
Source0:	https://xyzcmd.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1:	xyzcmd_ru.mo
Source2:	xyzcmd_uk.mo
Patch0:     	xyzcmd-0.0.5-locale.patch     
License:	LGPL
Group:		System Environment/Shells
URL:		https://xyzcmd.syhpoon.name
Requires:	python2-urwid
BuildArch:  	noarch
BuildRequires:  python2

%description
XYZCommander is a pure console visual file manager.

%prep
%setup -q
%patch0 -p1 -b .locale

%build
python2 setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{python2_sitelib}/libxyz
python2 setup.py install --no-compile --root $RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/xyzcmd.pot
%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/ru/LC_MESSAGES/xyzcmd.po*
%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/uk/LC_MESSAGES/xyzcmd.po*
# temporary workaround (until locale will be fixed in upstream)
%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/ru/LC_MESSAGES/xyzcmd.mo
%{__install} -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/ru/LC_MESSAGES/xyzcmd.mo
%{__install} -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/uk/LC_MESSAGES/xyzcmd.mo

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog COPYING COPYING.LESSER README doc/*
%{_bindir}/xyzcmd
%{python2_sitelib}/libxyz/
%{python2_sitelib}/xyzcmd-0.0.5-py2.?.egg-info
%{_datadir}/%{name}
%{_mandir}/man1/xyzcmd.1.*

%changelog
* Thu Aug 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.5
- Rebuilt for Fedora
* Sun Jan 23 2011 Vlad V. Teterya <vlad@server-labs.com.ua> - 0.0.5-3
- Add ukrainian locale
- Fix typos in russian locale
* Sat Jan 22 2011 Vlad V. Teterya <vlad@server-labs.com.ua> - 0.0.5-2
- Fix docs and locale install
* Sat Jan 22 2011 Vlad V. Teterya <vlad@server-labs.com.ua> - 0.0.5-1
- Rebuild for fc14
