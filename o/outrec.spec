Summary: Record all audio output from the sound card
Name: outrec
Version: 0.0.3
Release: 1
Source0: http://ncu.dl.sourceforge.net/project/outrec/%{name}_%{version}.orig.tar.gz
License: GPL
Group: Applications/Multimedia
URL: http://outrec.sourceforge.net/
BuildArch: noarch
BuildRequires: gambas3-devel
Requires: gambas3-runtime, gambas3-gb-form, gambas3-gb-desktop, gambas3-gb-gui, gambas3-gb-gtk
Requires: sox, lame, mplayer, twolame, pulseaudio-utils, libnotify
Vendor: Luis Aguiar <techm3@gmail.com>

%description
This is a GUI (Graphical User Interface) made in gambas for “pa-clone” script
that let you to, record all sound card audio output of your computer using sox.
In other words, you can record everything you hear no matter if it is from a
website or your own computer.

%prep
%setup -q -n %{name}-%{version}.orig/src/%{name}

%build
gbc3 -a
gba3

%install
rm -rf %{buildroot}
install -Dm755 %{name}.gambas %{buildroot}/%{_bindir}/%{name}
install -Dm644 %{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

install -d %{buildroot}/%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=outRec
Comment=Record all audio output from the sound card
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=AudioVideo;Audio;
EOF

%clean
rm -rf %{buildroot}

%files
%doc CHANGELOG outrecguide.pdf
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Dec 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.3
- Initial package for OSSII
