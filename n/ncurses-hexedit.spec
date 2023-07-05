Name: ncurses-hexedit
Summary: Edit files/disks in hex, ASCII and EBCDIC
Version: 0.9.7
Release: 6.1
License: GPLv2
Group: Applications/Editors
Source0: https://www.rogoyski.com/adam/programs/hexedit/hexedit-%{version}.tar.gz
BuildRequires: ncurses-devel
URL: https://www.rogoyski.com/adam/programs/hexedit/

%description
Curses Hexedit is a full screen hex editor using the curses, ncurses , or pdcurses library. Some of it's features are:
    GPL'd. It's Free Software.
    Familiar setup, similar to Nortan's Diskedit
    File Selection widget for selecting a file to edit.
    Editing and Viewing disks in Linux and OpenBSD.
    Allows Inserting and Deleting bytes from the file.
    Highlights changes in the file in bold.
    Fast boyer-moore string and byte searches.
    Undo - keeps track of all changes, reverting back to original always possible.
    Start of a base conversion/calculator utility built in.
    Portable. This should run on any platform with a dialect of the curses library
    I'll support it. I wrote in all the features I wanted. Anything missing? I'll probably add it in.

%prep
%setup -q -n hexedit-%{version}

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/*
%exclude %{_datadir}/info/dir
%{_datadir}/info/hexedit.info.*
%{_mandir}/man1/hexedit.1.*

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.7
- Rebuilt for Fedora
