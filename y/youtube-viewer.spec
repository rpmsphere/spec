Name: youtube-viewer
Summary: A free utility for playing youtube-videos with MPlayer
Version: 3.7.4
Release: 1
Group: Applications/Internet
License: Artistic License 2.0
URL: https://github.com/trizen/youtube-viewer
Source0: %{name}-%{version}.tar.gz
Requires: mplayer
Requires: perl(Data::Dump)
Requires: perl(LWP::UserAgent)
Requires: perl(Term::ANSIColor)
Requires: perl(Term::UI)
Requires: perl(URI::Escape)
BuildRequires: perl-devel
BuildRequires: perl(Module::Build)
BuildRequires: perl-JSON-PP
BuildArch: noarch

%description
Youtube Viewer is a CLI application which can interact with Youtube.
It is written in Perl and its scope is to search and play Youtube-videos
at the best quality available without using a flash player.

%prep
%setup -q

%build
perl Build.PL --gtk-youtube-viewer
./Build

%install
./Build install --destdir %{buildroot} \
--install_path lib=%{_datadir}/perl5 \
--install_path arch=%{_datadir}/perl5 \
--install_path script=%{_bindir} \
--install_path bindoc=%{_mandir}/man1 \
--install_path libdoc=%{_mandir}/man3

%files
%{_bindir}/*
%{_datadir}/perl5/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.7.4
- Rebuilt for Fedora
