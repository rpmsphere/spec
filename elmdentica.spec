%define	name elmdentica
%define version 0.9.10
%define release 20101225

Summary:	A simple Identi.ca client with Elementary UI
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source:		%{name}-%version.tar.gz
# Common
##BuildRequires:	json-c-devel
# Enlightenment BR
BuildRequires:	libeina-devel
BuildRequires: 	eet-devel
BuildRequires:  evas-devel
BuildRequires:	ecore-devel
BuildRequires:	efreet-devel
BuildRequires:	embryo-devel
BuildRequires:	edje-devel
BuildRequires:	emotion-devel
BuildRequires:	e_dbus-devel
BuildRequires:	azy-devel

%description
A simple Identi.ca client with Elementary UI

%prep
%setup -q

%build
./autogen.sh --disable-static --prefix=/usr
%__make

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

#menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Internet" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL NEWS README
%_bindir/elmdentica
%_datadir/applications/elmdentica.desktop
%_datadir/locale/*/LC_MESSAGES/elmdentica.mo
%_datadir/pixmaps/elmdentica.png
%_datadir/elmdentica/themes/default.edj

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Jan 05 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
