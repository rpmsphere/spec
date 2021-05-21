Name:		roadsend-php
Version:	20090812
Release:	1
Group:		Development/PHP
Summary:        The Roadsend PCC Compiler for PHP
License:	GPLv2+
URL:		http://code.roadsend.com/pcc/
Source0:	http://code.roadsend.com/snaps/%{name}-%{version}.tar.bz2
BuildRequires:	bigloo >= 3.0c
BuildRequires:	curl-devel >= 7.15.1
BuildRequires:	indent
BuildRequires:	info
BuildRequires:  fcgi-devel
BuildRequires:	libxml2-devel
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:  sqlite-devel >= 3.0.0
BuildRequires:	texinfo
Requires:	bigloo-libs >= 3.0c
Requires:	indent
Requires(post): info
Requires(preun): info

%description
Roadsend Compiler for PHP produces optimized stand alone applications,
libraries, and Web applications from standard PHP source code. The compiler
produces native machine code, not PHP byte code, so no interpreter is
required. It is a new implementation of the PHP language and runtime
environment compatible with Zend PHP. It does not share any code with the
original PHP implementation.

%prep
%setup -q -n %{name}-%{version}

%build
export CFLAGS="%{optflags}"

./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --libdir=%{_libdir}/pcc \
    --sysconfdir=%{_sysconfdir} \
    --mandir=%{_mandir}/man1 \
    --infodir=%{_infodir} \
    --docdir=%{_docdir} \
    --with-pcre \
    --with-fcgi \
    --with-xml \
    --with-mysql \
    --with-sqlite3 \
    --with-gtk=no \
    --with-gtk2=yes

export LD_LIBRARY_PATH=`pwd`/libs
make

# make the manual
pushd doc/manual
    make
popd

%install
rm -rf %{buildroot}

export LD_LIBRARY_PATH=`pwd`/libs
%makeinstall

# cleanup
rm -f %{buildroot}%{_libdir}/pcc/*.a
rm -f %{buildroot}%{_libdir}/pcc/*.h

# prepare the manual
rm -rf html-manual
install -d html-manual/resources
install -m0644 doc/manual/html/*.html html-manual/
install -m0644 doc/resources/* html-manual/resources/

%clean
rm -rf %{buildroot}

%files
%doc html-manual/* doc/COMPILER-LICENSE doc/RUNTIME-LICENSE README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pcc.conf
%attr(0755,root,root) %{_libdir}/*
%attr(0755,root,root) %{_bindir}/pcc
%attr(0755,root,root) %{_bindir}/pcc.fcgi
%attr(0755,root,root) %{_bindir}/pcctags
%attr(0755,root,root) %{_bindir}/pdb


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Aug 12 2009 Harry Chen <harry.chen@ossii.com.tw> 20090812-1.fc11
- rebuild and update to 20090812
* Tue Sep 09 2008 Feather Mountain <john@ossii.com.tw> 2.9.7-1.ossii
- rebuild and update to 2.9.7
* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.9.5-4mdv2009.0
+ Revision: 260277
- rebuild
* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.9.5-3mdv2009.0
+ Revision: 251329
- rebuild
* Thu Feb 21 2008 Oden Eriksson <oeriksson@mandriva.com> 2.9.5-1mdv2008.1
+ Revision: 173474
- 2.9.5
- rediffed P0
* Mon Jan 21 2008 Oden Eriksson <oeriksson@mandriva.com> 2.9.4-0.1mdv2008.1
+ Revision: 155676
- fix deps (curl-devel)
- import roadsend-php
* Mon Jan 21 2008 Oden Eriksson <oeriksson@mandriva.com> 2.9.4-0.1mdv2008.1
- initial Mandriva package (WIP)
