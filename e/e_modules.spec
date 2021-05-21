Summary: 	Loose collection of third party E17 modules
Name: 		e_modules
Version: 	0.0.1
Release: 	20101225
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%version.tar.gz
Patch1:		e_modules-0.0.1-20090227_e_util_dialog.patch
BuildRequires:	evas-devel
BuildRequires:	ecore-devel 
BuildRequires:	edje-devel 
BuildRequires:	edje
BuildRequires:	efreet-devel
BuildRequires:	enlightenment-devel
BuildRequires:  embryo-devel
BuildRequires:	embryo
BuildRequires:	e_dbus-devel
BuildRequires:	libelementary-devel
BuildRequires:  eweather-devel
BuildRequires:	ethumb-devel
BuildRequires:	emprint
Buildrequires:	gettext-devel
Buildrequires:  libxkbfile-devel
Buildrequires:	ImageMagick
Buildrequires:  libXcomposite-devel
BuildRequires:	libmpd-devel
BuildRequires:	cvs
Requires:	emprint

%description
e_modules is a loose collection of third party E17 modules written by
various authors.  They are not officially a part of E17, but they are
allowed to use the E cvs repository.  The modules are all separate
modules, written by separate authors.

%prep
%setup -q

%build
%define Werror_cflags %nil
./autogen.sh --disable-static --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

##rm -fr %buildroot%{_libdir}/enlightenment/modules/mixer
rm -fr %buildroot%_includedir/drawer %buildroot%_libdir/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS README
%{_libdir}/enlightenment/modules/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Fri Jan 21 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sun Dec 26 2010 Texstar <texstar at gmail.com> 20101226-1pclos2010
- update from svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
