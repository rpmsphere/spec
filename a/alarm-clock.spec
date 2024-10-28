Summary:        Alarm Clock for the GNOME desktop
Summary(de):    Wecker für den GNOME-Desktop
Name:           alarm-clock
Version:        1.4.3
Release:        12.4
License:        GPLv3
URL:            https://gtk-apps.org/content/show.php/Alarm+Clock?content=74469
Source:         %{name}-%{version}.tar.bz2
Group:          Graphical desktop/GNOME
BuildRequires: glib2-devel 
BuildRequires: intltool
BuildRequires: gtk2-devel
BuildRequires: GConf2-devel
#BuildRequires: libglade-devel
BuildRequires: gstreamer-devel
BuildRequires: libgnomeui-devel
BuildRequires: libnotify-devel
BuildRequires: mate-panel-devel
BuildRequires: unique-devel
BuildRequires: fedora-logos w3m udisks2
Requires: pygtk2
Requires: gstreamer-plugins-base
Requires: python-inotify

%description
Alarm Clock is a small alarm panel applet developed in Python
for GNOME/GTK desktop environments. It supports sound fading,
scheduled alarms, snooze option, passive window reminders,
exception lists for scheduled alarms, exporting alarms
and much more!

%description -l de
Alarm Clock ist ein privater Wecker für die GNOME-Desktopumgebung.
Er unterstützt Soundübergänge, passive und normale Dialoge, Vollbilddialoge
Weckpläne, Kommandozeilenaufrufe und einige Standardaktionen. 

#french
%description -l fr
Alarm Clock est une petite applet panneau d'alarme développé en Python
pour GNOME / GTK environnements de bureau. Il soutient la décoloration du son,
prévue alarmes, option snooze, rappels fenêtre passive,
des listes d'exceptions pour les alarmes programmées, l'exportation des alarmes
et beaucoup plus!

#spanish
%description -l es
Alarm Clock es un pequeño applet de panel de alarma desarrollado en Python
para GNOME / GTK entornos de escritorio. Es compatible con la decoloración de sonido,
las alarmas programadas, opción de despertador, recordatorios ventana pasiva,
listas de excepciones para las alarmas programadas, alarmas de exportación
y mucho más!

#polish
%description -l pl
Budzik jest mały applet panelu alarm opracowane w Pythonie
dla GNOME / GTK środowisku graficznym. Obsługuje dźwięk blaknięcie,
zaplanowane alarmów, opcja drzemki, pasywne przypomnienia oknie
list wyjątkiem regularnych alarmy, wywozu alarmy
i wiele więcej!

#serbian
%description -l sr
Аларм је аларм, мали панела развијен у Пытхон
за ГНОМЕ / ГТК + десктоп окружења. Он подржава звучне бледи,
заказана аларма, могућност обнављања, пасивно прозор подсетнике,
Изузетно листе заказана за аларме, аларме извоз
и још много тога!

#dutch
%description -l nl
Alarm Clock is een klein alarm panel applet ontwikkeld in Python
voor GNOME / GTK desktop omgevingen. Het ondersteunt geluid vervagen,
gepland alarm, snooze-optie, passieve venster herinneringen,
uitzondering lijsten voor geplande alarmen, alarmen exporteurs
en nog veel meer!

%prep
%setup -q
sed -i -e '216,218d' -e 's|NULL, NULL|NULL|' src/alarm_runner.c

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mv $RPM_BUILD_ROOT%{_datadir}/icons $RPM_BUILD_ROOT%{_datadir}/pixmaps
%find_lang %{name}

%files -f %{name}.lang
%{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.3
- Rebuilt for Fedora
* Mon Jul 05 2010 slick50 <lxgator@gmail.com> 1.4.1-1pclos2010
- 1.4.1
* Mon May 31 2010 slick50 <lxgator@gmail.com> 1.4-1pclos2010
- 1.4
* Mon Jan 11 2010 slick50 <lxgator@gmail.com> 1.3-1pclos2010
- 1.3
* Mon Nov 16 2009 slick50 <lxgator@gmail.com> 1.2.5-1pclos2010
- 1.2.5
* Thu Oct 01 2009 slick50 <lxgator@gmail.com> 1.2.4-1pclos2010
- 1.2.4
* Mon Sep 07 2009 slick50 <lxgator@gmail.com> 1.2.3-2pclos2009
- add patch0,1
* Wed Aug 05 2009 slick50 <lxgator@gmail.com> 1.2.2-1pclos2009
- 1.2.2
* Wed Jul 29 2009 slick50 <lxgator@gmail.com> 1.2.1-1pclos2009
- initial pkg
