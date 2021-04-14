Summary:	The GNU Lyric Display System
Name:		lyricue
Version:	4.0.13
Release:	1
License:	GPL
Group:		Applications/Multimedia
URL:		http://www.lyricue.org/
Source0:	http://www.lyricue.org/archive/%{name}-%{version}.tar.gz
BuildRequires:  libpng-devel
BuildRequires:	intltool
BuildRequires:	gtk2-devel
BuildRequires:	clutter-gtk-devel
#BuildRequires:	clutter-gst-devel
BuildRequires:	mysql-devel
BuildRequires:	sane-backends-devel
BuildRequires:  avahi-devel
BuildRequires:  avahi-glib-devel
Requires:	mysql
Requires:	mysql-libs
Requires:	perl-DBD-mysql
Requires:	perl-Gnome2-Canvas
Requires:	perl-Gtk2-Spell
Requires:	perl-URI

%description
This application is used to edit/display song lyrics and passages of
text on a second screen/projector for use at live events such as
church services, concerts and seminars.

%prep
%setup -q

%build
./autogen.sh --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
/usr/etc/lyricue
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/help/C/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/doc/%{name}
/usr/etc/apport/crashdb.conf.d/*
%{_datadir}/apport/package-hooks/*

%changelog
* Fri Dec 28 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.13
- Rebuilt for Fedora
* Mon Aug 03 2009 slick50 <lxgator@gmail.com> 2.0.0-1pclos2009
- initial pkg
