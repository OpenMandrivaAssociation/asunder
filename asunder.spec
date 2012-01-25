Summary:	GTK+-based audio CD ripper and encoder
Name:		asunder
Version:	2.1
Release:	1
License:	GPLv2
Group:		Archiving/Cd burning
URL:		http://littlesvr.ca/asunder/
Source0:	http://littlesvr.ca/asunder/releases/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libcddb)

Requires:	cdparanoia
Suggests:	lame
Suggests:	vorbis-tools
Suggests:	flac
Suggests:	wavpack

%description
Asunder is a graphical Audio CD ripper and encoder for Linux. You can 
use it to save tracks from an Audio CD as WAV, MP3, OGG, Musepack, AAC,
Monkey Audio, and/or FLAC.

%prep
%setup -q

# fix icon name in .desktop file
perl -pi -e 's,%{name}.png,%{name},g' %{name}.desktop

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

