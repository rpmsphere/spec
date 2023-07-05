Name:          bot-sentry
Version:       1.3.0
Release:       3.4
Summary:       Pidgin plugin to prevent Instant Message (IM) spam
Group:         Graphical Desktop/Applications/Networking
URL:           https://sourceforge.net/projects/pidgin-bs/
Source:        https://garr.dl.sourceforge.net/sourceforge/pidgin-bs/%{name}-%{version}.tar.bz2
License:       GPL
Obsoletes:     pidgin-bs, gaim-bs
BuildRequires: libpng-devel
BuildRequires: intltool >= 0.40.0
BuildRequires: pidgin-devel

%description
Bot Sentry is a Pidgin (libpurple) plugin to prevent Instant Message(IM) spam.
It allows you to ignore IMs unless the sender is in your Buddy List,
the sender is in your Allow List, or the sender correctly answers a question
you have predefined.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README README.mingw
%{_libdir}/purple-2/*.la
%{_libdir}/purple-2/*.so

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0
- Rebuilt for Fedora

* Mon Aug 25 2008 Tiziana Ferro <tiziana.ferro@email.it> 1.3.0-1mamba
- package created by autospec
