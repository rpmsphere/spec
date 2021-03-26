%undefine _missing_build_ids_terminate_build

Name:scratch	
Version: 1.4.0.1
Release: 1%{?dist}.bin
Summary: Programming system and content development tool
Group: Lifelong Kindergarten Group at the MIT Media Lab
License: MIT
URL: http://scratch.mit.edu	
Source0: http://info.scratch.mit.edu/sites/infoscratch.media.mit.edu/files/file/scratch-1.4.0.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libv4l, libv4l-devel

%description
Scratch is a programming language that makes it easy to create your own
interactive stories, animations, games, music, and art -- and share your
creations on the web.

%prep
%setup -q -n %{name}

%build
make

%install
rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{_libdir}/%{name}
install -m 644 Scratch.image %{buildroot}%{_libdir}/%{name}/.
install -m 644 Scratch.ini %{buildroot}%{_libdir}/%{name}/.
install -m 755 -d %{buildroot}%{_libdir}/%{name}/Plugins
install -m 644 Plugins/* %{buildroot}%{_libdir}/%{name}/Plugins/.

install -m 755 -d %{buildroot}%{_datadir}/%{name}/Help/en/images
install -m 644 Help/en/*.pdf %{buildroot}%{_datadir}/%{name}/Help/en/.
install -m 644 Help/en/*.html %{buildroot}%{_datadir}/%{name}/Help/en/.
install -m 644 Help/en/*.gif %{buildroot}%{_datadir}/%{name}/Help/en/.
install -m 644 Help/en/images/*.gif %{buildroot}%{_datadir}/%{name}/Help/en/images/.

install -m 755 -d %{buildroot}%{_datadir}/%{name}/locale
install -m 644 locale/* %{buildroot}%{_datadir}/%{name}/locale/.

cp -R Media  %{buildroot}%{_datadir}/%{name}/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Backgrounds/Indoors
#install -m 644 Media/Backgrounds/Indoors/* %{buildroot}%{_datadir}/%{name}/Media/Backgrounds/Indoors/.
#
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Backgrounds/Nature
#install -m 644 Media/Backgrounds/Nature/* %{buildroot}%{_datadir}/%{name}/Media/Backgrounds/Nature/.
#
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Backgrounds/Outdoors
#install -m 644 Media/Backgrounds/Outdoors/* %{buildroot}%{_datadir}/%{name}/Media/Backgrounds/Outdoors/.
#
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Backgrounds/Sports
#install -m 644 Media/Backgrounds/Sports/* %{buildroot}%{_datadir}/%{name}/Media/Backgrounds/Sports/.
#
#install -m 644 Media/Backgrounds/scratchthumbs.db %{buildroot}%{_datadir}/%{name}/Media/Backgrounds/.
#install -m 644 Media/Backgrounds/*.gif %{buildroot}%{_datadir}/%{name}/Media/Backgrounds/.
#
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Animals
#install -m 644 Media/Costumes/Animals/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Animals/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Fantasy
#install -m 644 Media/Costumes/Fantasy/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Fantasy/.
#
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/auto
#install -m 644 Media/Costumes/Letters/auto/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/auto
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/bubbles
#install -m 644 Media/Costumes/Letters/bubbles/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/bubbles
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/circles
#install -m 644 Media/Costumes/Letters/circles/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/circles
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/curly
#install -m 644 Media/Costumes/Letters/curly/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/curly
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/digital
#install -m 644 Media/Costumes/Letters/digital/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/digital
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/funky
#install -m 644 Media/Costumes/Letters/funky/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/funky
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/keys
#install -m 644 Media/Costumes/Letters/keys/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/keys
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/outline
#install -m 644 Media/Costumes/Letters/outline/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/outline
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/scratch
#install -m 644 Media/Costumes/Letters/scratch/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/scratch
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/stone
#install -m 644 Media/Costumes/Letters/stone/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Letters/stone
#
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Animals
#install -m 644 Media/Costumes/Animals/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Animals/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/People
#install -m 644 Media/Costumes/People/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/People/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Things
#install -m 644 Media/Costumes/Things/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Things/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Costumes/Transportation
#install -m 644 Media/Costumes/Transportation/* %{buildroot}%{_datadir}/%{name}/Media/Costumes/Transportation/.
#
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Sounds/Animal
#install -m 644 Media/Sounds/Animal/* %{buildroot}%{_datadir}/%{name}/Media/Sounds/Animal/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Sounds/Effects
#install -m 644 Media/Sounds/Effects/* %{buildroot}%{_datadir}/%{name}/Media/Sounds/Effects/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Sounds/Electronic
#install -m 644 Media/Sounds/Electronic/* %{buildroot}%{_datadir}/%{name}/Media/Sounds/Electronic/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Sounds/Human
#install -m 644 Media/Sounds/Human/* %{buildroot}%{_datadir}/%{name}/Media/Sounds/Human/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Sounds/Instruments
#install -m 644 Media/Sounds/Instruments/* %{buildroot}%{_datadir}/%{name}/Media/Sounds/Instruments/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Sounds/Music\ Loops
#install -m 644 Media/Sounds/Music\ Loops/* %{buildroot}%{_datadir}/%{name}/Media/Sounds/Music\ Loops/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Sounds/Percussion
#install -m 644 Media/Sounds/Percussion/* %{buildroot}%{_datadir}/%{name}/Media/Sounds/Percussion/.
#install -m 755 -d %{buildroot}%{_datadir}/%{name}/Media/Sounds/Vocals
#install -m 644 Media/Sounds/Vocals/* %{buildroot}%{_datadir}/%{name}/Media/Sounds/Vocals/.

install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Animation
install -m 644 Projects/Animation/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Animation/.
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Games
install -m 644 Projects/Games/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Games/.
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Greetings
install -m 644 Projects/Greetings/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Greetings/.
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Interactive\ Art
install -m 644 Projects/Interactive\ Art/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Interactive\ Art/.
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Music\ and\ Dance
install -m 644 Projects/Music\ and\ Dance/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Music\ and\ Dance/.
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Names
install -m 644 Projects/Names/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Names/.
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Sensors\ and\ Motors
install -m 644 Projects/Sensors\ and\ Motors/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Sensors\ and\ Motors/.
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Simulations
install -m 644 Projects/Simulations/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Simulations/.
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Speak\ Up
install -m 644 Projects/Speak\ Up/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Speak\ Up/.
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Stories
install -m 644 Projects/Stories/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Stories/.

install -m 644 license.txt %{buildroot}%{_datadir}/%{name}/.
install -m 644 ACKNOWLEDGEMENTS %{buildroot}%{_datadir}/%{name}/.
install -m 644 KNOWN-BUGS %{buildroot}%{_datadir}/%{name}/.

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 src/scratch %{buildroot}%{_bindir}/.
install -m 755 App/scratch_squeak_vm %{buildroot}%{_bindir}/.

install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 src/man/scratch.1.gz %{buildroot}%{_mandir}/man1/.
install -m 644 src/man/scratch_squeak_vm.1.gz %{buildroot}%{_mandir}/man1/.

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 src/%{name}.desktop %{buildroot}%{_datadir}/applications/.

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 src/icons/48x48/scratch.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/.
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -m 644 src/icons/128x128/scratch.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/.
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes
install -m 644 src/icons/48x48/gnome-mime-application-x-scratch-project.png %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/.
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes
install -m 644 src/icons/128x128/gnome-mime-application-x-scratch-project.png %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes/.

install -m 755 -d %{buildroot}%{_datadir}/mime/packages
install -m 644 src/%{name}.xml %{buildroot}%{_datadir}/mime/packages/.

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ACKNOWLEDGEMENTS KNOWN-BUGS license.txt README.txt
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/48x48/mimetypes/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/icons/hicolor/128x128/mimetypes/*

%changelog
* Thu Dec 29 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat May 08 2010 Kevin Somervill <ksomervi@brokenlogo.com>
- Initial package
