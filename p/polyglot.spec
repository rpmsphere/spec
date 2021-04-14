Name:           polyglot
Version:        1.4.70b
Release:        7.1
Summary:        Xboard protocol to UCI protocol adapter
License:        GPLv2+
Group:          Games/Boards
URL:            http://hardy.uhasselt.be/Toga/polyglot-release/
Source0:        http://hardy.uhasselt.be/Toga/polyglot-release/%{name}-%{version}.tar.gz

%description
PolyGlot is a "UCI adapter".  It connects a GUI interface (such as
XBoard, Winboard, Arena or Chessbase) to a UCI chess engine.

By specifying an opening book (in PolyGlot book format) chess engines
can transparently use such books.

PolyGlot understands the two main GUI protocols: UCI and xboard.
Normally the protocol will be auto detected but this can be overridden
in the configuration file.

In xboard mode PolyGlot fully translates between the xboard and UCI
protocols.  In addition it tries to solve known problems with other
adapters.  For instance, it detects and reports draws by fifty-move
rule, repetition, etc ... It also supports Chess960.

When in UCI mode PolyGlot mostly passes commands from the GUI to the
engine and vice versa, except that it will play book moves on behalf of
the engine when the occasion arises.

The engine options are exported as UCI options in UCI mode and as
"feature option=" commands in xboard mode. The latter form an extension
of the xboard protocol as defined by H.G. Muller.

Options which normally appear in the [PolyGlot] section of the config
file (see below) are exported as options with their name prefixed by
"Polyglot". This makes it easy to filter them in the GUI.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure --bindir=%{_bindir} --datadir=%{_datadir}
make

%install
%make_install
rm -fr %{buildroot}%{_docdir}/%{name}

%files
%doc AUTHORS ChangeLog INSTALL NEWS TODO README* book_format.html
%{_bindir}/*
%{_mandir}/man6/%{name}.6*

%changelog
* Fri Feb 20 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.70b
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 1.4.70b-5.mga5
+ Revision: 748010
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 1.4.70b-4.mga5
+ Revision: 687718
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 1.4.70b-3.mga4
+ Revision: 517611
- Mageia 4 Mass Rebuild
* Sun Jan 13 2013 umeabot <umeabot> 1.4.70b-2.mga3
+ Revision: 378044
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sun Dec 02 2012 kamil <kamil> 1.4.70b-1.mga3
+ Revision: 324729
- new version 1.4.70b
* Wed Jul 25 2012 kamil <kamil> 1.4.67b-1.mga3
+ Revision: 274355
- imported package polyglot
