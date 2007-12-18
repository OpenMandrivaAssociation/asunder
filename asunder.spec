Summary:	GTK+-based ISO image editor
Name:		asunder
Version:	1.0
Release:	%{mkrel 1}
Source0:	http://littlesvr.ca/asunder/releases/%{name}-%{version}.tar.bz2
License:	GPLv2
Group:		Archiving/Cd burning
URL:		http://littlesvr.ca/isomaster/
BuildRequires:	gtk+2-devel
BuildRequires:	libcddb-devel
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick
Requires:	cdparanoia
Suggests:	vorbis-tools
Suggests:	flac

%description
Asunder is a graphical Audio CD ripper and encoder for Linux. You can
use it to save tracks from an Audio CD as WAV, OGG, and/or FLAC.

%prep
%setup -q
# fix icon name in .desktop file
perl -pi -e 's,%{name}.png,%{name},g' %{name}.desktop
%configure2_5x

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %name

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
convert -scale 48 pixmaps/%{name}.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png 
convert -scale 32 pixmaps/%{name}.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 pixmaps/%{name}.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%post
%{update_icon_cache hicolor}
%{update_menus}
%{update_desktop_database}
%postun
%{clean_icon_cache hicolor}
%{clean_menus}
%{clean_desktop_database}

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
