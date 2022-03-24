Name: mps-youtube
Summary: Terminal based YouTube jukebox with playlist management
Version: 0.2.5
Release: 3
Group: utils
License: Free Software
URL: https://github.com/np1/mps-youtube
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: desktop-file-utils
#Requires: python3-pafy
#Requires: mpv
#Requires: |
#Requires: mplayer2,
#Requires: ffmpeg
#Requires: |
#Requires: libav-tools,
#Requires: python3,
#Requires: python3:any
#Requires: python3-pkg-resources

%description
This project is a terminal based YouTube client with an interactive text
interface and in-built help. It can be used to search YouTube, create local
playlists to queue your favourite content, play audio or video (launched in
external player) and can download YouTube content in various formats (mp4,
flv, webm, ogg, m4a, m4v and 3gp).

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=/usr

%files
%{_bindir}/mpsyt
%{python3_sitelib}/mps_youtube*
%{_datadir}/applications/%{name}.desktop
#%{_datadir}/doc/%{name}
#%{_mandir}/man1/mpsyt.1.gz

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.5
- Rebuilt for Fedora
