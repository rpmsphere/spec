%undefine _debugsource_packages
Name:          anagramarama
Version:       0.2
Release:       1
Summary:       A FREE word game for Linux
Group:         Graphical Desktop/Applications/Educational
URL:           http://www.coralquest.com/anagramarama/
Source:        http://www.omega.clara.net/anagramarama/dist/%{name}-%{version}.tar.gz
Source1:       anagramarama.png
Patch1:        anagramarama.install.patch
License:       GPL
BuildRequires: SDL-devel
BuildRequires: SDL_mixer-devel
BuildRequires: SDL-devel >= 1.2.8, SDL_mixer-devel >= 1.2.6

%description
The aim is to find as many words as possible in the time available. Get the
longest word and you'll advance to the next level.

%prep
%setup -q -n %{name}
%patch1 -p1

%build
%__make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/%{name}-%{version}/audio
mkdir -p %{buildroot}/usr/share/%{name}-%{version}/images
mkdir -p %{buildroot}/usr/bin

install -D -m 644 audio/*.wav %{buildroot}/usr/share/%{name}-%{version}/audio/
install -D -m 644 images/*bmp %{buildroot}/usr/share/%{name}-%{version}/images/
install -m 755 wordlist.txt %{buildroot}/usr/share/%{name}-%{version}/
install -m 755 ag %{buildroot}/usr/bin

#Icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Create the system menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=A FREE word game for Linux
Exec=ag
Icon=%{_datadir}/pixmaps/anagramarama.png
Terminal=0
Type=Application
Categories=Education;
EOF

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/%{name}-%{version}/audio/*.wav
%{_datadir}/%{name}-%{version}/images/*.bmp
%{_datadir}/%{name}-%{version}/*.txt
%{_datadir}/applications/anagramarama.desktop
%{_datadir}/pixmaps/anagramarama.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Mon Jun 29 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.2-2mamba
- specfile updated and rebuilt
* Tue Jul 19 2005 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 0.2-1qilnx
- package created by autospec
