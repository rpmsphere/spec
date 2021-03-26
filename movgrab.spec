%define _name Movgrab

Name:		movgrab
Version:	3.1.2
Release:	3.1
License:	GPL
Group:		Video
URL:		https://github.com/ColumPaget/Movgrab
Source:		https://github.com/ColumPaget/Movgrab/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Summary:	Command-line movie downloader
Summary(de):	Konmmandozeilen Video Downloader

%description
Movgrab is a downloader for all those pesky sites that insist 
you use a big fat browser that runs flash in order to see 
their content. It's a command-line application written in 
straight C, and so doesn't require you to install perl. 
Nor ruby. Nor python. Nor guile, scheme, glib, gtk, qt, gnome, 
kde, X-windows, m4, firefox or windows. No! Not any of that! 
It *should* compile on all posix unix systems.

%description -l de
Movgrab ist ein Downloader für all jene nervtötenden Webseiten, 
die einen dicken, fetten Browser lahm legen, weil Flash läuft, 
um den Inhalt sehen zu können. 
Es ist eine Kommandozeilen-Anwendung in C geschrieben und so ist 
es nicht erforderlich, Perl zu installieren. Auch nicht Rubin. 
Oder Python. Auch benötigt es nicht irgendeine Regelung von 
glib, gtk, qt, GNOME, KDE, X-Windows, M4, Firefox oder Fenstern. 
Nein! Nichts von all dem! Es *sollte* auf allen POSIX 
Unix-Systemen kompiliert werden können.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 0755 %{name} %buildroot%_bindir/%{name}

%files
%{_bindir}/%{name}
%doc CHANGES LICENCE README Docs

%changelog
* Fri Jul 21 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1.2
- Rebuild for Fedora
* Mon Dec 23 2013 billybot <billybot> 1.2.1-2pclos2013
- tweak specfile
* Sat Dec 21 2013 daniel <meisssw01 at gmail.com> 1.2.1-1free2013
- upstream tarball
* Mon Oct 22 2012 daniel <meisssw01 at gmail.com> 1.1.12-1leiche2012
- upstream tarball
* Sun Apr 29 2012 leiche <meisssw01 at gmail.com> 1.1.10-1pclos2012
- 1.1.10
* Thu Mar 22 2012 leiche <meisssw01 at gmail.com> 1.1.9-1pclos2012
- 1.1.9
* Thu Feb 23 2012 leiche <meisssw01 at gmail.com> 1.1.8-1pclos2012
- 1.1.8
* Tue Jan 17 2012 leiche <meisssw01 at aol.com> 1.1.6-1leiche2012
- 1.1.6
* Fri Dec 16 2011 leiche <meisssw01 at aol.com> 1.1.5-1leiche2011
- import to PCLinuxOS
