%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:	Visual editor for edje file
Name:		editje
Version:	0.9.3
Release:	20101225
License: 	BSD
Group: 		Graphical desktop/Enlightenment
Source:		%{name}-%{version}.tar.gz
Source1:	%name.desktop
URL:		http://www.enlightenment.org/
BuildRequires:	edje-devel
BuildRequires:	edje
BuildRequires: 	evas-devel
Buildrequires:	ecore-devel
BuildRequires:  flex
BuildRequires:  desktop-file-utils
Requires: 	edje
Requires:	python-ecore 
Requires:	python-evas
Requires:	python-elementary
Requires:	python-edje
Requires:	python-e_dbus
Obsoletes:	edje_editor

%description
Editje is an Edje editor oriented towards UI design, 
and not just being a GUI over the edc syntax.
It provides three major modes: standard edition, 
animations and signals management.

%prep
%setup -q

%build
./autogen.sh
%configure --disable-static
%__make

%install
rm -rf %buildroot
%makeinstall

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc  AUTHORS COPYING* README
%{_bindir}/editje-bin
%{_datadir}/application-registry/editje.applications
%{_datadir}/applications/editje.desktop
%{_datadir}/editje/data/sample/sample-anim.edj
%{_datadir}/editje/data/sample/sample.edj
%{_datadir}/editje/data/templates/default.edj
%{_datadir}/editje/data/themes/default.edj
%{_datadir}/icons/editje.png
%{python_sitelib}/editje/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Jan 04 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
