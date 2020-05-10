<?php
namespace NethServer\Module\Dashboard\Applications;
/*
 *
 * This script is part of NethServer.
 *
 * NethServer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * NethServer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with NethServer.  If not, see <http://www.gnu.org/licenses/>.
 */
/**
 * Discourse web interface
 *
 * @author Stephane de Labrusse <stephdl@de-labrusse.fr>
 */
class Discourse extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{
    public function getName()
    {
        return "Discourse";
    }
    public function getInfo()
    {
        $vhost = $this->getPlatform()->getDatabase('configuration')->getProp('discourse','domain');
        if ($vhost) {
            return array(
            'url' => "https://".$vhost
            );
        }
    }
}
