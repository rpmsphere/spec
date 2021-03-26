Name: typer
Summary: GNOME Typing Learner/Trainer
Version: 0.4.2
Release: 11.1
Group: Applications/Education
License: GPLv3+
URL: http://code.google.com/p/gnome-typer
Source0: http://gnome-typer.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires:  atk-devel
BuildRequires:  cairo-devel
BuildRequires:  cairo-gobject-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gtk3-devel
BuildRequires:  pango-devel
BuildRequires:  fortune-mod
#BuildRequires:  gmodule-devel
BuildRequires:  libgnomekbd-devel
#BuildRequires:  gnomekbdui-devel
BuildRequires:  libxklavier-devel
Requires:  fortune-mod

%description
Typer is a graphical GNOME tutor for learning and training keyboard typing.
Features keyboard layout, lessons, text file, fortune support and stats.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/pixmaps

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/doc/%{name}

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuild for Fedora
* Fri May 17 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.2-1
- Update
* Wed May 08 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.0-1
- ChangeLog Start
