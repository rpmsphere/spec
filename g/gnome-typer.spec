Name: gnome-typer
Summary: GNOME Typing Learner/Trainer
Version: 0.4.2
Release: 11.1
Group: Applications/Education
License: GPLv3+
URL: https://code.google.com/p/gnome-typer
Source0: https://gnome-typer.googlecode.com/files/typer-%{version}.tar.bz2
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
%setup -q -n typer-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_datadir}/doc/typer %{buildroot}%{_datadir}/doc/%{name}
mv %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/pixmaps/typer.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mv %{buildroot}%{_bindir}/typer %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_datadir}/applications/typer.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's|typer|gnome-typer|' %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/doc/%{name}

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuilt for Fedora
* Fri May 17 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.2-1
- Update
* Wed May 08 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.0-1
- ChangeLog Start
